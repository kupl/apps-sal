class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # GOOGLE - Union Find Alg
        # For graph approach (DFS) it will work for a small input. In worst case we will have 20K elem
        # and we will need to do 20K^2=20*20*10^6 coparison if two num has a common factor.
        # Time limit will exceed. Therefore use Union Find here.
        parent = [-1] * 100001

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xp = find(x)
            yp = find(y)
            if xp != yp:
                parent[yp] = xp

        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    union(i, x)
                    union(x, x // i)

        count = 0
        hashmap = {}
        for x in A:
            xp = find(x)
            count = max(count, 1 + hashmap.get(xp, 0))
            hashmap[xp] = 1 + hashmap.get(xp, 0)
        return count

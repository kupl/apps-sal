class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = {}
        rank = {i: 1 for i in range(len(A))}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if rank[px] > rank[py]:
                    px, py = py, px
                rank[py] += rank[px]
                uf[px] = py

        def primeFactor(x):
            ans = set()
            if not x % 2:
                ans.add(2)
                while not x % 2: x //= 2
            for i in range(3, int(math.sqrt(x)) + 1, 2):
                if not x % i:
                    ans.add(i)
                    while not x % i: x //= i
            if x > 1: ans.add(x)
            return ans

        dic = {}
        for i in range(len(A)):
            for j in primeFactor(A[i]):
                dic.setdefault(j, i)
                union(i, dic[j])
        cnt = Counter()
        for i in range(len(A)):
            cnt[find(i)] += 1
        return max(cnt.values())

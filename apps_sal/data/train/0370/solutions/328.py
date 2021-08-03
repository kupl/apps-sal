class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        root = list(range(max(A) + 1))

        def find(i):
            while not root[i] == i:
                root[i] = root[root[i]]
                i = root[i]
            return i

        def union(a, i):
            root[find(a)] = find(i)

        for a in A:
            for i in range(2, int(math.sqrt(a)) + 1):
                if a % i == 0:
                    union(a, i)
                    union(a, a // i)
        return Counter([find(a) for a in A]).most_common()[0][1]

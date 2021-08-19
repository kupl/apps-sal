class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        uf = {}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[find(x)] = find(y)
        for (i, a) in enumerate(A):
            if not a % 2:
                union(A[i], 2)
                if a // 2 > 1:
                    union(A[i], a // 2)
            while not a % 2:
                a //= 2
            for k in range(3, int(sqrt(A[i])) + 1, 2):
                if not a % k:
                    union(A[i], k)
                    if a // k > 1:
                        union(A[i], a // k)
                while not a % k:
                    a //= k
                if a == 1:
                    break
            if a > 1:
                union(A[i], a)
        return max(Counter([find(a) for a in A]).values())

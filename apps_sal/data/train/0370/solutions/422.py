class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        N = len(A)
        parent = list(range(N))
        size = [1] * N

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            if size[x] < size[y]:
                x, y = y, x

            parent[y] = x
            size[x] += size[y]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        ftoi = {}
        for i, n in enumerate(A):
            for factor in range(2, floor(sqrt(n)) + 1):
                if n % factor == 0:
                    for f in (factor, n // factor):
                        if f in ftoi:
                            union(i, ftoi[f])
                        else:
                            ftoi[f] = i
            if n in ftoi:
                union(i, ftoi[n])
            else:
                ftoi[n] = i

        return max(size)

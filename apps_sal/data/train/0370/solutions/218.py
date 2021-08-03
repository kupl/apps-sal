class Solution:
    def largestComponentSize(self, A):
        p = list(range(max(A) + 1))

        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        def union(x, y):
            p[find(x)] = p[find(y)]

        for a in A:
            for k in range(2, int(math.sqrt(a) + 1)):
                if a % k == 0:
                    union(a, a // k)
                    union(a, k)
        return collections.Counter([find(a) for a in A]).most_common(1)[0][1]

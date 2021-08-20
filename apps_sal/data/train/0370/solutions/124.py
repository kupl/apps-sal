class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        fa = [i for i in range(len(A))]
        sz = [1] * len(A)

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        factor = defaultdict(list)
        for i in range(len(A)):
            x = A[i]
            for y in range(2, int(math.sqrt(x)) + 1):
                if not x % y:
                    factor[y].append(i)
                    while not x % y:
                        x //= y
            if x > 1:
                factor[x].append(i)
        for (k, v) in list(factor.items()):
            for j in range(1, len(v)):
                (x, y) = (v[0], v[j])
                (fx, fy) = (find(x), find(y))
                if fx != fy:
                    if sz[fx] > sz[fy]:
                        sz[fy] += sz[fx]
                        fa[fx] = fy
                    else:
                        sz[fx] += sz[fy]
                        fa[fy] = fx
        ans = 0
        for i in range(len(fa)):
            if i == fa[i]:
                ans = max(ans, sz[i])
        return ans

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        @lru_cache(maxsize=None)
        def dfs(i, k, i0):
            if k > (n - i):
                return 0
            if k == 1:
                return position[n - 1] - position[i0]
            if k == 0:
                return 1e20

            d = 0
            for j in range(i, n):
                d_new = dfs(j + 1, k - 1, j)
                d = max(min(d_new, position[j] - position[i0]), d)

            return d

        @lru_cache(None)
        def f(i, k):
            if k == 0:
                return float('inf')
            if i == len(position):
                return float('-inf')

            ret = f(i + 1, k)
            for x in range(i + 1, len(position)):
                v = min(position[x] - position[i], f(x, k - 1))
                ret = max(ret, v)

            return ret

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

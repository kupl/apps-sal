class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        @lru_cache(maxsize=None)
        def dfs(i, k, i0):
            # put k balls into position[i:] with max min force
            # i0 is the position with the largest index between position[0] and position[i-1]
            # d0 is the max min force between balls placed between position[0] and position[i-1]
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

        # return dfs(1, m-1, 0)

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

        # return f(0, m-1)

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

    # position = [1,2,3,4,7], m = 3, n=5
    # dfs(0, 3, -1e20, 1e20)
    # i=0, k=3, n-i=5
    # j=0, d0_new = 1e20,
    # dfs(1, 2, 0, 1e20): d_new = ?
    # dfs(2, 2, 1, 1e20): d_new = ?
    # dfs(3, 2, 2, 1e20): d_new =
    # dfs(4, 2, 3, 1e20): k=2 > 5-4=1, d_new = 0

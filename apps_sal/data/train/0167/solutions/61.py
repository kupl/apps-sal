# More specifically, to get the k that best fits each drop, we don't need to go over all floors from 1 to j.
# As for a fixed k, dp[i][k] goes up as k increases. This means dp[i-1][k-1] will increase and dp[i][j-k] will
# decrease as k goes from 1 to j. The optimal value of k will be the middle point where the two meet. So to
# get the optimal k value for dp[i][j], we can do a binary search for k from 1 to j.


class Solution(object):
    def superEggDrop(self, K, N):
        def dfs(i, j):
            if i == 1:
                return j
            if j == 0:
                return 0
            if j == 1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            while lo < hi:
                mid = (lo + hi) // 2
                left, right = dfs(i - 1, mid - 1), dfs(i, j - mid)
                # print(mid, left, right)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            res = 1 + max(dfs(i - 1, lo - 1), dfs(i, j - lo))
            d[i, j] = res
            return res

        d = {}
        return dfs(K, N)

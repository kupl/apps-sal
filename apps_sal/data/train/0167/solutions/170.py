class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = {}

        def helper(K, N):
            if N <= 1:
                dp[(K, N)] = N
            if K == 1:
                dp[(K, N)] = N

            if (K, N) not in dp:
                l = 1
                r = N
                while l + 1 < r:
                    mid = (l + r) // 2
                    # if egg breaks at midpoint, try egg drop for lower floors
                    die = helper(K - 1, mid - 1)
                    # if egg survives, try egg drop for higher floors
                    live = helper(K, N - mid)

                    if die < live:
                        l = mid
                    elif die > live:
                        r = mid
                    else:
                        l = r = mid
                dp[(K, N)] = 1 + min([max(helper(K - 1, l - 1), helper(K, N - l)), max(helper(K - 1, r - 1), helper(K, N - r))])
            return dp[(K, N)]

        return helper(K, N)

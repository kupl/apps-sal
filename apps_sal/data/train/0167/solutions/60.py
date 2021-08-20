class Solution:

    def superEggDrop(self, K: int, N: int) -> int:

        def dfs(k, n):
            if k == 1:
                return n
            if n <= 1:
                return n
            if (k, n) in memo:
                return memo[k, n]
            (l, r) = (0, n)
            while l < r:
                mid = l + (r - l) // 2
                (left_num, right_num) = (dfs(k - 1, mid - 1), dfs(k, n - mid))
                if right_num > left_num:
                    l = mid + 1
                else:
                    r = mid
            memo[k, n] = 1 + max(dfs(k - 1, l - 1), dfs(k, n - l))
            return memo[k, n]
        memo = {}
        return dfs(K, N)

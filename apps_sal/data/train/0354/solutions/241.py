class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0 for k in range(16)]for j in range(6)]for i in range(5000)]

        M = 10 ** 9 + 7

        def dfs(dies, last, cur_len):
            if not dies:
                # print(curr_roll)
                return 1

            if last >= 0 and dp[dies][last][cur_len] > 0:
                return dp[dies][last][cur_len]

            ret = 0

            for i in range(6):
                if cur_len == rollMax[i] and i == last:
                    continue

                nxt = 0

                if last == i:
                    nxt = cur_len + 1
                else:
                    nxt = 1

                ret += dfs(dies - 1, i, nxt)
                ret %= M

            if last >= 0:
                dp[dies][last][cur_len] = ret

            return ret

        return dfs(n, -1, 0)

class Solution:

    def mp_gen(self):
        dp = [[0] * 32 for _ in range(32)]
        dp[0][0] = 1
        mp = {}
        for i in range(32):
            for j in range(32):
                k = 2 ** i * 3 ** j
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                mp[k] = dp[i][j]
        return mp

    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        cnt = 0
        st = set()
        st.add(n)
        while st:
            cnt += 1
            st_temp = set()
            for v in st:
                if v == 1:
                    return cnt
                st_temp.add(v - 1)
                if v % 2 == 0:
                    st_temp.add(v // 2)
                if v % 3 == 0:
                    st_temp.add(v // 3)
            st = st_temp
        return -1

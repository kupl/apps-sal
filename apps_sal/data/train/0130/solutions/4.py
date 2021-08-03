class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        b = ord('0')
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            cnt = 0
            num = ord(s[i]) - b
            while num <= k:
                cnt += dp(i + 1) % MOD
                i += 1
                if i < n:
                    num = num * 10 + ord(s[i]) - b
                else:
                    break
            return cnt % MOD

        return dp(0)

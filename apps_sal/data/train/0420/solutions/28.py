class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        bits = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        dp = {0: -1}
        (ans, state) = (0, 0)
        for (i, c) in enumerate(s):
            if c in bits:
                state ^= 1 << bits[c]
            ans = max(ans, i - dp.get(state, 128))
            dp[state] = min(dp.get(state, 128), i)
        return ans

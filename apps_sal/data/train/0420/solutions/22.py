class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        (vowels, bits, dp) = ({'a', 'e', 'i', 'o', 'u'}, {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}, {0: -1})
        (res, odds) = (0, set())
        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] in odds:
                    odds.discard(s[i])
                else:
                    odds.add(s[i])
            key = 0
            for o in odds:
                key |= 1 << bits[o]
            if key in dp:
                res = max(res, i - dp[key])
            else:
                dp[key] = i
        return res

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        s = s + 'a'
        bits, dp = {'a':0,'e':1,'i':2,'o':3,'u':4}, {0:-1}
        res = 0
        key = 0
        for i, char in enumerate(s):                
            if char in bits:
                if key in dp:
                    res = max(res, i-dp[key] - 1)
                key = key ^ (1 << bits[char])
                if key not in dp:
                    dp[key] = i
        return res


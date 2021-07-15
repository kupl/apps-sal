class Solution:
    def numSplits(self, s: str) -> int:
        s_len = len(s)
        if s_len == 0 or s_len == 1:
            return  0
        seen = set()
        dp = [0 for _ in range(s_len-1)]
        dp[0] = 1
        seen.add(s[0])
        for i in range(1,s_len-1):
            if s[i] in seen:
                dp[i] = dp[i-1]
            else:
                seen.add(s[i])
                dp[i] = dp[i-1]+1
        
        seen = set()
        acc = 0
        count = 0
        for i in range(s_len-1,0,-1):
            if (s[i] not in seen):
                seen.add(s[i])
                acc += 1
            if (acc == dp[i-1]):
                count += 1
        return count



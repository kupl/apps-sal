class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        last_dp = [str2[:j] for j in range(len(str2) + 1)]
        
        for i in range(1, len(str1) + 1):
            dp = [str1[:i]]
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp.append(last_dp[j - 1] + str1[i - 1])
                else:
                    if len(last_dp[j]) < len(dp[j - 1]):
                        dp.append(last_dp[j] + str1[i - 1])
                    else:
                        dp.append(dp[j - 1] + str2[j - 1])
            last_dp = dp
            
        return last_dp[-1]


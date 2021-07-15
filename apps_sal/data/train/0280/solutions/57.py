class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        len_s = len(s)
        if K >= len_s: return 0
        dp = [[float('inf')] * (K + 1) for _ in range(len_s + 1)]
        
        s = '0' + s
        dp[0][0] = 0
        for i in range(1, len_s + 1):
            for k in range(1, min(K + 1, i + 1)):
                for j in range(k, i + 1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + self.helper(s, j, i))
        return dp[-1][-1]
    
    def helper(self, sub_s, l_idx, r_idx):
        # 计算将sub_s转换为回文数，需要最少的操作字符数
        count = 0
        while l_idx < r_idx:
            if sub_s[l_idx] != sub_s[r_idx]:
                count += 1
            l_idx += 1
            r_idx -= 1
        return count

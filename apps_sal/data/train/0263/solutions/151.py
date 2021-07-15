class Solution:
    def knightDialer(self, n: int) -> int:
        d = {
            0:(4, 6),
            1:(6, 8),
            2:(7, 9),
            3:(4, 8),
            4:(3, 9, 0),
            5:(),
            6:(1, 7, 0),
            7:(2, 6),
            8:(1, 3),
            9: (2, 4)
        }
        dp = [1] * 10
        for _ in range(n-1):
            temp = [0] * 10
            for i in range(10):
                for j in d[i]:
                    temp[j] = dp[i] + temp[j]
            dp = temp
        
      
        return sum(dp) % (10 ** 9 + 7)

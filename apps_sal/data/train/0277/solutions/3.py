class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        dp = [0] * (n+1)
        dp[0] = 2
        max_so_far = moment = 0
        
        for num in light:
            max_so_far = max(num, max_so_far)
            if dp[num-1] == 2:
                dp[num] = 2
                
                for b in range(num+1, max_so_far+1):
                    if dp[b] == 1:
                        dp[b] = 2
                    else:
                        break
                if dp[max_so_far] == 2: moment += 1
            else:
                dp[num] = 1
                
        return moment

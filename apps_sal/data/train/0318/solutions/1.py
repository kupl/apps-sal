class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        rounds = n//3
        
        def num_s(slices):
            # print(slices)
            n = len(slices)
            dp = [i for i in slices]
            for i in range(rounds):
                maxx = 0
                dp2 = [0]*(i*2)
                for j in range(i*2,n):
                    # print(j)
                    if i == 0:
                        dp2.append(max(maxx,slices[j]))
                        maxx = dp2[j]
                    else:
                        dp2.append(max(maxx,slices[j] + dp[j-2]))
                        maxx = dp2[j]
                dp = dp2     
                # print(dp, slices)
            return dp[len(dp)-1]
        
        return max(num_s(slices[1:]),num_s(slices[:n-1]))

            
            

        


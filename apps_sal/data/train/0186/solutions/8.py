class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0]
        for i in range(1,target+1):
            result = 0
            for j,c in enumerate(cost):
                if i<c:
                    continue
                if dp[i-c] == 0 and i!=c:
                    continue
                result = max(result,10*dp[i-c]+j+1)
            dp.append(result)
        return str(dp[-1])

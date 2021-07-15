class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        
        dp = {0: 0}
        counter = [0] * len(pre)
        
        for i in range(1, len(pre)):
            if pre[i] - target in dp:
                idx = dp[pre[i] - target]
                counter[i] = max(counter[i-1], counter[idx] + 1)
            else:
                counter[i] = counter[i-1]
            dp[pre[i]] = i
        return counter[-1]

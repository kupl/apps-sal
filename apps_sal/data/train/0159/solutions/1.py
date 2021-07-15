from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums.copy()
        ans = dp[0]

        monoq = deque()
        qsize = 0
        
        for i, num in enumerate(nums):
            if i > 0:   
                dp[i] = max(dp[i], num + monoq[0][0])
            ans = max(ans, dp[i])
            
            pops = 1
            while monoq and dp[i] > monoq[-1][0]:
                _, freq = monoq.pop()
                pops += freq
                qsize -= freq
            monoq.append([dp[i], pops])
            qsize += pops

            while qsize > k:
                extra = qsize - k
                if monoq[0][1] > extra:
                    monoq[0][1] -= extra
                    qsize = k
                else:
                    _, v = monoq.popleft()
                    qsize -= v
            
        return ans


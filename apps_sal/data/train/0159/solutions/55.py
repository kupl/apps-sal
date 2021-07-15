from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums, k):
        N, queue = len(nums), deque()
        dp = [0] * N
        for i, val in enumerate(nums):
            if queue and (i - queue[0] > k):
            #if i > k and (queue[0] == i - k - 1):
                queue.popleft()
            #dp[i] = (val + max(dp[queue[0]], 0)) if queue else val
            if queue and dp[queue[0]] > 0:
                dp[i] = val + dp[queue[0]]
            else:
                dp[i] = val
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        return max(dp)
        
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums, k):
        if not nums or not k: return 0
        if max(nums) <= 0: return max(nums)
        if min(nums) >= 0: return sum(nums)
        queue, N = deque(), len(nums)
        for i in range(N):
            #if queue and (i - queue[0] > k):
            while queue and queue[0] < i - k:
                queue.popleft()
            # compute the max sum we can get at index i
            if queue:
                nums[i] += nums[queue[0]]
            # delet all the sequence that smaller than current sum, becaus there will never be
            # considers ==> smaller than current sequence, and end before current sequence
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            # if nums[i] < 0, it can't be a useful prefix sum
            if nums[i] > 0:
                queue.append(i)
        return max(nums)
    
    
    
from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums, k):
        N, queue = len(nums), deque()
        dp = [val for val in nums]
        for i, val in enumerate(nums):
            if queue and (i - queue[0] > k):
                queue.popleft()
            if queue and dp[queue[0]] > 0:
                dp[i] += dp[queue[0]]
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        return max(dp)


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        stack = deque()
        
        for i in range(len(nums)):
            nums[i] += stack[0] if stack else 0
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if i >= k and stack and stack[0] == nums[i-k]:
                stack.popleft()
            if nums[i] > 0:
                stack.append(nums[i])
        return max(nums)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        q = deque()
        for i in range(len(nums)):
            nums[i] += q[0] if q else 0
            while q and nums[i] > q[-1]:
                q.pop()
            if nums[i] > 0:
                q.append(nums[i])
            if i >= k and q and q[0] == nums[i-k]:
                q.popleft()
        return max(nums)

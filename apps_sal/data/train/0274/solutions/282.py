class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        min_deque, max_deque = collections.deque(), collections.deque()
        l = r = 0
        
        while r < len(nums):
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if max_deque[0] < l:
                    max_deque.popleft()
                if min_deque[0] < l:
                    min_deque.popleft()
            
            ans = max(ans, r-l+1)
            r += 1
            
        return ans

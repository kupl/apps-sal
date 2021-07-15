class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        l = r = 0
        ans = 0
        while r < len(nums):
            num = nums[r]
            while max_q and nums[max_q[-1]] <= num:
                max_q.pop()
            while min_q and nums[min_q[-1]] >= num:
                min_q.pop()
            max_q.append(r)
            min_q.append(r)
            
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                l += 1
                if l > max_q[0]:
                    max_q.popleft()
                if l > min_q[0]:
                    min_q.popleft()
            ans = max(ans, r - l + 1)
            r+=1
        return ans


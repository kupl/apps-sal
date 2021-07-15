class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Use sortedList to maintain the max/min of the subarray 
        from sortedcontainers import SortedList
        wd = SortedList([nums[0]])  # window
        max_len = 1
        
        l = 0
        r = 0
        while r < len(nums):
            minn = wd[0]
            maxx = wd[-1]
            if maxx-minn <= limit:
                max_len = max(max_len, r-l+1)
                # extend right
                r += 1
                if r < len(nums):
                    wd.add(nums[r])
            else:
                # shrink left
                wd.discard(nums[l])
                l += 1
        return max_len

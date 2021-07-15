from bisect import insort

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        win = []
        n = len(nums)
        i = j = 0
        max_len = 0
        
        while j < n:
            if not win:
                win.append(nums[j])
            else:
                insort(win, nums[j])

            while win[-1] - win[0] > limit:
                win.remove(nums[i])
                i += 1
                
            if j - i + 1 > max_len:
                max_len = j - i + 1
                
            j += 1
                
        return max_len
    
# time: O(n^2)
# space: O(n)


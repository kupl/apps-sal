class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_elements = collections.deque()
        min_elements = collections.deque()
        
        max_len = 0
        i = 0
        for j, num in enumerate(nums):
            while max_elements and max_elements[-1] < num:
                max_elements.pop()
            while min_elements and min_elements[-1] > num:
                min_elements.pop()
            max_elements.append(num)
            min_elements.append(num)
            
            while max_elements[0] - min_elements[0] > limit:
                if max_elements and max_elements[0] == nums[i]:
                    max_elements.popleft()
                if min_elements and min_elements[0] == nums[i]:
                    min_elements.popleft()
                i += 1
                
            max_len = max(max_len, j - i + 1)
            
        return max_len

from collections import deque, Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        q = deque()
        lowest = 0
        nums = sorted(set(nums))
        for i in range(len(nums)):
            if i and nums[i] != nums[i - 1] + 1 and lowest:
                return False
            
            diff = counter[nums[i]] - lowest
            if diff < 0:
                return False
            
            if diff > 0:
                q.appendleft((i + k - 1, diff))
                
            lowest = counter[nums[i]]
            
            if q[-1][0] == i:
                lowest -= q.pop()[1]
            
        return not q

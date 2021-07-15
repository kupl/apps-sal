class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        multiple = 0
        last = 0
        
        #@lru_cache(None)
        def find(mx):
            nonlocal last
            if mx <= 1:
                return mx
            if mx % 2 == 1:
                return find(mx-1)+1
            last += 1
            return find(mx//2)+1
        
        result = 0
        for i, n in enumerate(nums):
            result += find(n)-last
            multiple = max(multiple, last)
            last = 0
            
        return result + multiple


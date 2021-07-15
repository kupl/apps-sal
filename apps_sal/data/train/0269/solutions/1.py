class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        N = len(nums)
        past, curr = -1, 0
        
        for curr in range(N):
            if nums[curr] == 1:
                if past < 0:
                    past = curr
                elif curr-past > k:
                    past = curr
                else:
                    return False
            
        
        return True

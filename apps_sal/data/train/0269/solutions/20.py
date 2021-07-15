class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        locs = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                locs[i] = True
        
        key= list(locs.keys())
        for i in range(len(key)-1):
            if key[i+1] - key[i] - 1 < k:
                return False
        
        return True


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         if len(nums) % k or len(nums) < k:
#             return false
        
#         ktrack = 0
        
#         nums.sort()
        
#         for n in nums:
        nums.sort()
        
        index = {}
        for i in nums:
            index[i] = index.get(i,0) + 1
            
        for i in index:
            # subtracting from dict count until nothing left
            # k-size lists must be asc
            while index[i] > 0:
                # creating window for k-size list
                for j in range(i,i+k):
                    # if j still has any left, decrement
                    if index.get(j,0) > 0:
                        index[j] -= 1
                    else:
                        return False
        return True


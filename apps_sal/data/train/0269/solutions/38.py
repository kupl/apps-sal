class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = float('-inf')
        for i, x in enumerate(nums):
            if x==1:
                if i-1-last<k:
                    return False
                last = i
        return True

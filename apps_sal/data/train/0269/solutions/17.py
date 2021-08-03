class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        position = -1
        for index, item in enumerate(nums):
            if item & 1:
                if index - position - 1 < k and position != -1:
                    return False
                position = index
        return True

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not k:
            return True

        pre_index = -1
        for i, val in enumerate(nums):
            if val:
                if pre_index != -1 and i - pre_index - 1 < k:
                    return False
                pre_index = i
        return True

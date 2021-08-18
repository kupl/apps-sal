class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        prev_one_ind = -1
        for i, v in enumerate(nums):
            if v == 1:
                if prev_one_ind >= 0:
                    diff = i - prev_one_ind - 1
                    if diff < k:
                        return False
                prev_one_ind = i

        return True

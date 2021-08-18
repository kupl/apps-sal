class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last1 = -1
        tally = len(nums)
        for idx, val in enumerate(nums):

            if val == 1:
                last1 = idx
                if tally < k:
                    return False
                tally = 0
            else:
                tally += 1

        return True

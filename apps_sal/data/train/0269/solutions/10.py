class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = []
        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)
        true = 0
        false = 0
        for j in range(len(pos) - 1):
            if pos[j + 1] - pos[j] <= k:
                return False
        return True

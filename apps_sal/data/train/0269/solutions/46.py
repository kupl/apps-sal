class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = 0
        while pos < len(nums):
            try:
                pos = nums.index(1, pos)
                pos2 = nums.index(1, pos + 1)
            except:
                break
            if pos2 - pos - 1 < k:
                return False
            pos = pos2
        print(pos)
        return True

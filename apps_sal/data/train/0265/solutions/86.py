class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = {0: True}
        sm = 0
        count = 0
        for i in nums:
            sm += i
            if sm - target in d:
                count += 1
                sm = 0
                d = {0: True}
            else:
                d[sm] = True
        return count

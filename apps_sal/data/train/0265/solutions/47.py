class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        sums = set()
        s = 0
        cnt = 0
        sums.add(0)

        for n in nums:
            s += n
            if s - target in sums:
                cnt += 1
                sums = set()

            sums.add(s)

        return cnt

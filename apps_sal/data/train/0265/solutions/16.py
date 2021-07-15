class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count = 0
        sums = set()
        sums.add(0)
        tot = 0
        for num in nums:
            tot += num
            if (tot - target) in sums:
                count += 1
                sums=set()
            sums.add(tot)
        return count


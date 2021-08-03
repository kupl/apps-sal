class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count, sums, curr = 0, {0}, 0
        for num in nums:
            curr += num
            if curr - target in sums:
                count += 1
                sums.clear()
            sums.add(curr)
        return count

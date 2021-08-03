class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        count = 0
        total = 0
        pastSums = set()

        for n in nums:
            total += n

            if total == target or total - target in pastSums:
                total = 0
                count += 1
                pastSums.clear()
            else:
                pastSums.add(total)

        return count

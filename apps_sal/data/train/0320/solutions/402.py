class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def nrOfOpsToZero(n):
            if n == 0:
                return (0, 0)
            if n % 2 == 1:
                recDups, recIncs = nrOfOpsToZero(n - 1)
                return (recDups, recIncs + 1)
            recDups, recIncs = nrOfOpsToZero(n // 2)
            return (recDups + 1, recIncs)
        maxDups = 0
        totalIncs = 0
        for i in range(0, len(nums)):
            dups, incs = nrOfOpsToZero(nums[i])
            totalIncs += incs
            maxDups = max(maxDups, dups)
        return int(maxDups + totalIncs)

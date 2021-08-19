class Solution:

    def minOperations(self, nums: List[int]) -> int:
        numreps = []
        for num in nums:
            numreps.append(self.numToOps(num))
        numops = 0
        max2s = 0
        for rep in numreps:
            numops += rep[1]
            if rep[2] > max2s:
                max2s = rep[2]
        return numops + max2s

    def numToOps(self, val):
        rep = {1: 0, 2: 0}
        while val:
            if val % 2:
                rep[1] += 1
                val = val - 1
            else:
                rep[2] += 1
                val = int(val / 2)
        return rep

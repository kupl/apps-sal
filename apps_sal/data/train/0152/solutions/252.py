class Solution:
    def isSolution(self, m, position, minforce):
        index = 0
        remaining = m
        for bin in position:
            if bin >= index:
                remaining -= 1
                index = bin + minforce
            if remaining == 0:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        maxDist = position[-1]
        minDist = 0
        while maxDist > minDist + 1:
            average = (minDist + maxDist) // 2
            if Solution.isSolution(self, m, position, average):
                minDist = average
            else:
                maxDist = average
        if Solution.isSolution(self, m, position, maxDist):
            return maxDist
        else:
            return minDist

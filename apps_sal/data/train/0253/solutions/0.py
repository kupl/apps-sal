class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(machines) % len(machines) != 0:
            return -1
        mean = sum(machines) // len(machines)
        cum, step = 0, 0
        for x in machines:
            cum += x - mean
            step = max(step, abs(cum), x - mean)
        return step

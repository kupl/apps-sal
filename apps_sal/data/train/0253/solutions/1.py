class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        length = len(machines)
        if total % length != 0:
            return -1

        avg = int(total / length)
        cum = 0
        target = 0
        result = 0
        for m in machines:
            cum += m
            target += avg
            max_share = m - avg
            result = max(result, abs(target - cum), max_share)

        return result

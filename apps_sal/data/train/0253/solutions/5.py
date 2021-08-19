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
        cnt = 0
        result = 0
        for m in machines:
            cnt += m - avg  # load-avg is "gain/lose"
            result = max(result, abs(cnt), m - avg)
        return result

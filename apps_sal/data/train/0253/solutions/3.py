class Solution:

    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        if sum(machines) % n != 0:
            return -1
        s = sum(machines)
        k = s // n
        presum = 0
        right = 0
        max_net = 0
        for i in range(n):
            presum += machines[i]
            left = -right
            right = presum - k * (i + 1)
            net = left + right
            max_net = max(max_net, abs(left), abs(right), net)
        return max_net

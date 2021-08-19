class Solution:

    def __init__(self):
        pass

    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        N = len(machines)
        if N == 0:
            return 0
        val_sum = sum(machines)
        if val_sum % N != 0:
            return -1
        val_each = val_sum // N
        (go_left, go_right, net_change, max_step) = (0, 0, 0, 0)
        for i in range(N):
            go_left = -go_right
            go_right = go_right + machines[i] - val_each
            net_change = go_left + go_right
            step = max(abs(go_left), abs(go_right), net_change)
            max_step = max(max_step, step)
        return max_step

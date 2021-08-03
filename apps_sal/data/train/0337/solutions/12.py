class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        left = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(left) < 0:
            return -1
        tank, start = 0, 0
        for i in range(len(left)):
            tank += left[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

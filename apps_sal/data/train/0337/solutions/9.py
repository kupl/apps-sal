class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        fuel = totalGas = totalCost = start = 0
        for i in range(len(cost)):
            totalGas += gas[i]
            totalCost += cost[i]
            fuel = fuel + gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0

        return start if totalGas >= totalCost else -1

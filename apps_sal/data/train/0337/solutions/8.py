class Solution:

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(gas)):
            res.append(gas[i] - cost[i])
        max_sum = 0
        max_index = 0
        a = [0 for x in range(len(res))]
        for i in range(len(res)):
            max_sum = max(res[i] + max_sum, res[i])
            if max_sum == res[i]:
                max_index = i
                max_sum = res[i]
        temp = (max_index + 1) % len(gas)
        gas_sum = res[max_index]
        while temp != max_index:
            gas_sum += res[temp]
            temp = (temp + 1) % len(gas)
        if gas_sum >= 0:
            return max_index
        else:
            return -1

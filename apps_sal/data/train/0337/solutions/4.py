class Solution:

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        total = len(gas)
        travel = 0
        start = -total
        current = start
        print(('start:', start))
        while travel < total:
            tank += gas[current] - cost[current]
            travel += 1
            current += 1
            if current == total:
                return -1
            print((current, '\ttank:', tank, gas[current], cost[current], '\ttravel:', travel))
            if tank < 0:
                tank = 0
                jump = current - start
                start += jump
                travel -= jump
                print(('reset Start:', start, tank))
        return start + total

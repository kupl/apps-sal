class Solution:

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        (cf, s, e) = (0, 0, 0)
        found = False
        while True:
            nextHop = gas[e] - cost[e]
            if cf + nextHop >= 0:
                e = (e + 1) % len(gas)
                cf = cf + nextHop
                if s == e:
                    found = True
                    break
                else:
                    continue
            else:
                if s == e:
                    s = (s + 1) % len(gas)
                    e = s
                else:
                    cf += -gas[s] + cost[s]
                    s = (s + 1) % len(gas)
                if s == 0:
                    break
        return s if found else -1

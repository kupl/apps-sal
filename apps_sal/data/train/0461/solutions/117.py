class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ret = [-1] * n

        def computeFor(i):
            mana = manager[i]
            if mana == -1:
                return 0
            return getVal(mana) + informTime[mana]

        def getVal(i):
            if ret[i] == -1:
                ret[i] = computeFor(i)
            return ret[i]
        return max((getVal(i) for i in range(n)))

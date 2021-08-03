class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # ret[i] is num minutes from start until employee i knows about it
        ret = [-1] * n

        def computeFor(i):
            mana = manager[i]
            if mana == -1:
                # is head of company
                return 0
            # otherwise manager needs to learn, then informTime
            return getVal(mana) + informTime[mana]

        def getVal(i):
            # cached computation
            if ret[i] == -1:
                ret[i] = computeFor(i)
            return ret[i]

        return max(getVal(i) for i in range(n))

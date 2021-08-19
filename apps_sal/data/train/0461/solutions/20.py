class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        delays = [-1] * n

        def delay(id: int):
            if delays[id] >= 0:
                return delays[id]
            myman = manager[id]
            if myman < 0:
                delays[id] = 0
                return 0
            mandelay = delay(myman) + informTime[myman]
            delays[id] = mandelay
            return delays[id]
        return max((delay(i) for i in range(n)))

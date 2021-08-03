from sortedcontainers import SortedList


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        turned = SortedList()
        ret = 0

        for turn in light:
            turned.add(turn)
            if len(turned) == turned[-1]:
                ret += 1

        return ret

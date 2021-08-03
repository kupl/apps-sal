from sortedcontainers import SortedList


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        li = list()

        for i, n in enumerate(A):
            li.append((n, i))

        li.sort()

        ans = 0

        bt = SortedList()

        for pair in li:
            n = pair[0]
            i = pair[1]
            # print(bt)
            # print(i)
            if len(bt) == 0:
                bt.add(i)
                continue
            if bt[0] < i:
                if i - bt[0] > ans:
                    ans = i - bt[0]
            bt.add(i)

        return ans

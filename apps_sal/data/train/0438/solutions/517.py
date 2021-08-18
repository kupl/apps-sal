from sortedcontainers import SortedList


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        zeros = SortedList()
        zeros.add(0)
        zeros.add(len(arr) + 1)
        if len(arr) == m:
            return len(arr)
        for inverse_step, i in enumerate(arr[::-1], 1):
            head = zeros.bisect_left(i)
            if i - zeros[head - 1] - 1 == m:
                print((len(arr), inverse_step))
                return len(arr) - inverse_step

            tail = zeros.bisect_right(i)
            if zeros[tail] - i - 1 == m:
                return len(arr) - inverse_step

            zeros.add(i)
        return -1

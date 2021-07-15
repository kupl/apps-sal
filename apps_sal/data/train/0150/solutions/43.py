from sortedcontainers import SortedList

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left, right = SortedList(), SortedList(A)
        for i in range(len(A)-1):
            left.add(A[i])
            right.discard(A[i])
            if left[-1] <= right[0]:
                break
        return i + 1


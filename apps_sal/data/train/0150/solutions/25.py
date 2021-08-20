class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        least = [float('inf')] * len(A)
        for i in range(len(A) - 1, -1, -1):
            if i == len(A) - 1:
                least[i] = A[i]
            else:
                least[i] = min(least[i + 1], A[i])
        greatest = A[0]
        for i in range(1, len(A)):
            if greatest <= least[i]:
                break
            greatest = max(greatest, A[i])
        return i

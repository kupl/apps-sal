class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        mx = [-1] * len(A)
        mn = [-1] * len(A)
        for i in range(len(A)):
            if i == 0:
                mx[i] = A[i]
            else:
                mx[i] = max(A[i], mx[i - 1])
        for j in range(len(A) - 1, -1, -1):
            if j == len(A) - 1:
                mn[j] = A[j]
            else:
                mn[j] = min(A[j], mn[j + 1])
        for i in range(len(A) - 1):
            if mx[i] <= mn[i + 1]:
                return i + 1
        return len(A) - 1

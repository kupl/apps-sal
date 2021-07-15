class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # Track index of min from left
        idxsMin, res = [], 0
        for i, x in enumerate(A):
            if not idxsMin or A[idxsMin[-1]] > x:
                idxsMin.append(i)
        # Compare every element from right with the min element from left
        for j in range(len(A))[::-1]:
            while idxsMin and A[idxsMin[-1]] <= A[j]:
                res = max(res, j - idxsMin.pop())
        return res

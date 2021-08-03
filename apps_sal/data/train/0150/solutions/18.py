class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        length = len(A)
        leftMax = A[0]
        currMax = leftMax
        ret = 0

        for i in range(1, length):
            currMax = max(A[i], currMax)
            if leftMax > A[i]:
                leftMax = currMax
                ret = i

        return ret + 1

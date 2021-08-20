class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        result = 0
        tempDq = []
        A = [0] + A + [0]
        for idx in range(len(A)):
            while tempDq and A[tempDq[-1]] > A[idx]:
                prevIdx = tempDq.pop()
                lastIdx = tempDq[-1]
                result += A[prevIdx] * (prevIdx - lastIdx) * (idx - prevIdx)
            tempDq.append(idx)
        return result % (10 ** 9 + 7)

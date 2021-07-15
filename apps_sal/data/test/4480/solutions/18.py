class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        targetSum = sum(A) // 3
        a = 1
        runningSum = A[0]
        while a < len(A) and runningSum != targetSum:
            runningSum += A[a]
            a += 1
        b = len(A) - 2
        runningSum = A[-1]
        while b > -1 and runningSum != targetSum:
            runningSum += A[b]
            b -= 1
        return not a > b

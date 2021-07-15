class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        total = 0
        MOD = 10 ** 9 + 7
        powerSum = 2**0
        counter = 2
        currSum = A[0]
        for i in range(1, len(A)):
            total += (powerSum * A[i]) - currSum
            currSum *= 2
            currSum += A[i]
            powerSum += counter
            counter *= 2
           
       
        return total % MOD


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        return self.dp_bitwise(A)

    def dp_bitwise(self, A: List[int]) -> bool:
        #dummy case
        if (len(A) <= 1):
            return False
        #calculate sum and number of elements
        n = len(A)
        Sum = 0
        for x in A:
            Sum += x
        #dp[s] = m -- means sum s can be formed with elements of length bit i == 1 of m
        #e.g. dp[10] = 20 it means sum 10 can be achieved with 2 or 4 elements - 10100 
        #init dp with 0
        dp = [ 0 for _ in range(Sum+1)]
        dp[A[0]] = 2
        #we iterate through all the elements
        for i in range(1, n):
            #we check every possible sum 
            for s in range(Sum-A[i], -1, -1):
                #if s can be previously formed
                if dp[s] > 0:
                    # it means we can form s + A[i] also from dp[s] by shifting it 
                    # with one, as we have an additional element
                    dp[s + A[i]] |= (dp[s]<<1)
            dp[A[i]] |= 2
        
        for leng in range(1, n):
            if (Sum * leng) % n == 0 and ( (1 << leng) & dp[(Sum * leng) // n] ):
                return True
        return False

    


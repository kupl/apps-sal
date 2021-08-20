class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        return self.dp_bitwise(A)

    def dp_bitwise(self, A: List[int]) -> bool:
        if len(A) <= 1:
            return False
        n = len(A)
        Sum = 0
        for x in A:
            Sum += x
        dp = [0 for _ in range(Sum + 1)]
        dp[A[0]] = 2
        for i in range(1, n):
            for s in range(Sum - A[i], -1, -1):
                if dp[s] > 0:
                    dp[s + A[i]] |= dp[s] << 1
            dp[A[i]] |= 2
        for leng in range(1, n):
            if Sum * leng % n == 0 and 1 << leng & dp[Sum * leng // n]:
                return True
        return False

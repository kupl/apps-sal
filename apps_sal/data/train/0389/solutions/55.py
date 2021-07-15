class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total = sum(A)
        l = len(A)
        dp = [0] * (total + 1)
        dp[A[0]] = 2
        for i in range(1, l):
            for j in range(total - A[i], -1, -1):
                dp[j + A[i]] |= (dp[j] << 1)
            dp[A[i]] |= 2
        
        for i in range(1, l):
            if (total * i) % l == 0 and ((1 << i) & dp[total * i // l]) > 0:
                return True
        return False


class Solution:
    def numWays(self, steps: int, n: int) -> int:
        A = [0, 1]
        mod=10 ** 9 + 7
        for t in range(steps):
            A[1:] = [sum(A[i - 1:i + 2]) % mod for i in range(1, min(n + 1, t + 3))]
        return A[1] % mod        

class Solution:
    def formulaSum(self, N, L):
        return N/L - (L+1)/2
    
    def consecutiveNumbersSum(self, N: int) -> int:
        total = 0
        L = 1
        while L*(L+1)/2 <= N:
            a = self.formulaSum(N, L)
            if a - int(a) == 0.0:
                total += 1
            L += 1
        return total

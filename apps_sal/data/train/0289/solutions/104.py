class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumul = [0]
        for a in A:
            cumul.append(cumul[-1] + a)
            
        best = 0
        for i in range(len(A) - L - M + 1):
            for j in range(i + L, len(A) - M + 1):
                best = max(best, cumul[i + L] - cumul[i] + cumul[j + M] - cumul[j])
            for j in range(i + M, len(A) - L + 1):
                best = max(best, cumul[i + M] - cumul[i] + cumul[j + L] - cumul[j])
        return best

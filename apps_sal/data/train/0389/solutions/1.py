class Solution:
    def splitArraySameAverage(self, A):
        N, S, P = len(A), sum(A), [1]
        for a in A:
            P[1:] = [(p << a) | q for p, q in zip(P, P[1:] + [0])]
        return any(S * n % N == 0 and P[n] & (1 << (S * n // N))
               for n in range(1, N))

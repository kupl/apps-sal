class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
        1. create cumsum arr
        2. create arr of subarry sums from cumsum for L and M
        3. N^2 mix and match while ensuring the nums don't overlap

        '''

        cumsum = []
        for num in A:
            if not cumsum:
                cumsum.append(num)
            else:
                cumsum.append(cumsum[-1] + num)

        Lsums = [0] * len(A)
        Msums = [0] * len(A)

        if M > L:
            L, M = M, L

        for j in range(L - 1, len(A)):
            if j == L - 1:
                Lsums[j] = cumsum[j]
            else:
                Lsums[j] = cumsum[j] - cumsum[j - L]
        for j in range(M - 1, len(A)):
            if j == M - 1:
                Msums[j] = cumsum[j]
            else:
                Msums[j] = cumsum[j] - cumsum[j - M]

        out = 0
        for l in range(L - 1, len(A)):
            for m in range(M - 1, len(A)):
                if m <= l - L or m - M >= l:
                    out = max(out, Lsums[l] + Msums[m])
        return out

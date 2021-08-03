class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        idx = 0
        num_digits = len(A)
        A_bitrep = int('1' + ''.join([str(i) for i in A]), 2)

        K_bitrep = 2 ** K - 1
        num_flips = 0
        while A_bitrep > K_bitrep:
            if A_bitrep & 1 == 0:
                num_flips += 1
                A_bitrep ^= K_bitrep
            A_bitrep >>= 1

        return num_flips if A_bitrep == K_bitrep else -1

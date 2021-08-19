class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # special case for K = 1
        if K == 1:
            return N

        # initialize data
        Rp = [i for i in range(0, N + 1)]
        R = [0] * (N + 1)
        R[1] = 1

        k = 2
        while k <= K:
            l1 = 0
            for n in range(2, N + 1):
                # if n < 2**k:
                #    R[n] = n.bit_length()
                if Rp[n - l1 - 1] >= R[n - 1]:
                    R[n] = R[n - 1] + 1
                else:
                    R[n] = R[n - 1]

                if R[n] > R[n - 1]:
                    l1 = n - 1

            Rp, R = R, Rp
            k += 1

        return Rp[N]

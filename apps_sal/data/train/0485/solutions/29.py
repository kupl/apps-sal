class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # left bit needs to get flipped
        # flip left bit and the K-1 bits to the right
        # now consider

        #         counter = 0
        #         for i in range(len(A)-K+1):
        #             # print(i,A)
        #             if A[i] == 0:
        #                 counter += 1
        #                 for j in range(K):
        #                     A[i+j] ^= 1

        #         # return counter if sum(A) == len(A) else -1
        #         return counter if 0 not in A[-K:] else -1

        counter = 0
        q = []
        qL = 0

        for i in range(len(A) - K + 1):
            if A[i] == (len(q) - qL) % 2:  # then this bit would be a 0 after previous flips applied
                # flip at A[i]
                counter += 1
                q.append(i + K - 1)  # the last bit affected by this flip
            if qL < len(q) and q[qL] == i:
                qL += 1
            # print(q)
            # print(f'i:{i}, qL:{qL}, len(q), {len(q)}, top')

        # check the bits for which there's not enough room to flip at
        for i in range(len(A) - K + 1, len(A)):

            if A[i] == (len(q) - qL) % 2:
                # 0 0, 1 1
                return -1
            if qL < len(q) and q[qL] == i:
                qL += 1
            # print(q)
            # print(f'i:{i}, qL:{qL}, len(q), {len(q)}, top')

        return counter

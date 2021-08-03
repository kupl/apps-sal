class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        for i, x in enumerate(A):
            # check if the current index has been marked before
            # if True, then flip the \"flip\" var
            flip ^= hint[i]

            if x ^ flip == 0:  # If we must flip the subarray starting here...
                ans += 1  # We're flipping the subarray from A[i] to A[i+K-1]

                if i + K > N:
                    return -1

                flip ^= 1

                if i + K < N:
                    hint[i + K] = 1

        return ans

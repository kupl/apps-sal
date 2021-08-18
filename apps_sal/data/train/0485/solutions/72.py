class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:

        N = len(A)
        hint = [0] * N
        ans = flip = 0

        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:
                ans += 1
                if i + K > N:
                    return -1
                flip ^= 1
                if i + K < N:
                    hint[i + K] ^= 1
        return ans

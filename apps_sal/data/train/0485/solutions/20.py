class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        # when we flip a subarray like A[i], A[i+1], .., A[i+K-1]
        # we can instead flip our current writing state, and put a hint at position i+K to flip back
        # our writing state
        for i, x in enumerate(A):
            flip ^= hint[i]

            # if we must flip the subarray starting here...
            if x ^ flip == 0:
                ans += 1

                if i + K > N: return -1

                flip ^= 1
                if i + K < N: hint[i + K] ^= 1

        return ans

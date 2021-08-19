class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N
        ans = 0
        flip = 0
        for (i, x) in enumerate(A):
            if flip == hint[i]:
                flip = 0
            else:
                flip = 1
            if x == 1 and flip == 1 or (x == 0 and flip == 0):
                ans += 1
                if i + K > N:
                    return -1
                flip = 1 - flip
                if i + K < N:
                    hint[i + K] = 1 - hint[i + K]
        return ans

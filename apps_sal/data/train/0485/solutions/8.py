class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        store = [0] * len(A)
        ans = flip = 0

        for i, x in enumerate(A):
            flip ^= store[i]
            if x ^ flip == 0:
                ans += 1
                if i + K > len(A):
                    return -1
                flip ^= 1
                if i + K < len(A):
                    store[i + K] ^= 1
        return ans

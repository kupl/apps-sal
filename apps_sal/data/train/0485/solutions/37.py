class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = [0] * len(A)
        p = ans = 0
        for i in range(len(A)):
            if i >= K:
                # switch back
                p ^= flipped[i - K]
            if p == A[i]:
                if i + K > len(A):
                    return -1
                ans += 1
                flipped[i] = 1
                p ^= 1
        return ans

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # greedy
        n = len(A)
        flipped = res = 0
        isFlipped = [0] * n
        for i in range(n):
            # isFlipped[i-K] does not affect i here
            if (i >= K):
                flipped ^= isFlipped[i - K]
            if (flipped ^ A[i] == 0):
                if (i + K > n):
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1

        return res

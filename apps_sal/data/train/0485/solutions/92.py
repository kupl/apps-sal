class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = [False] * len(A)
        count = [0] * len(A)
        flips = 0

        for i in range(len(A)):
            if i > 0:
                x = flipped[i - K] if i >= K else 0
                count[i] = count[i - 1] - x

            if (A[i] + count[i]) % 2 == 0:
                count[i] += 1
                flipped[i] = True
                flips += 1

        return flips if not any(flipped[len(A) - K + 1:]) else -1

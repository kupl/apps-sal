class Solution:

    def minKBitFlips(self, A: List[int], k: int) -> int:
        c = 0
        flippedtill = [0 for i in range(len(A) + 1)]
        curr = 0
        if len(A) == k:
            if sum(A) == 0:
                return 1
            elif sum(A) == len(A):
                return 0
            else:
                return -1
        for i in range(len(A) - k + 1):
            curr = (curr + flippedtill[i]) % 2
            if (A[i] + curr) % 2 == 0:
                flippedtill[i + 1] += 1
                flippedtill[i + k] -= 1
                c += 1
        for i in range(len(A) - k + 1, len(A)):
            curr = (curr + flippedtill[i]) % 2
            if (A[i] + curr) % 2 == 0:
                return -1
        return c

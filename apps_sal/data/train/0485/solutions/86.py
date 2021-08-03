class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        is_flipped = [0] * len(A)
        flipped = result = 0

        for i in range(len(A)):
            if i >= K:
                flipped ^= is_flipped[i - K]

            if A[i] == flipped:
                if i + K > len(A):
                    return -1
                is_flipped[i] = 1
                flipped ^= 1
                result += 1

        return result

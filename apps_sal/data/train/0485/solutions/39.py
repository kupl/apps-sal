class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flip_count = 0
        hint = [0] * n
        min_flip = 0

        for i in range(n):
            if i >= K and hint[i - K] == 1:
                flip_count -= 1

            if flip_count % 2 == A[i]:
                if i + K > n:
                    return -1

                min_flip += 1
                flip_count += 1

                hint[i] = 1

        return min_flip

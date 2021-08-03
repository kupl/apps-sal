class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flip = 0
        current_flips = 0
        queue = []
        for i in range(n):

            if len(queue) > 0 and queue[0] + K == i:
                queue.pop(0)
                current_flips = current_flips - 1

            if (A[i] == 0 and current_flips % 2 == 0) or (A[i] == 1 and current_flips % 2 != 0):
                if i + K > n:
                    return -1
                queue.append(i)
                current_flips = current_flips + 1
                flip = flip + 1

        return flip

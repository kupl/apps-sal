class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        num = 0
        flip_queue = []
        flip_sum = 0
        for i in range(n - K + 1):
            if flip_sum & 1:
                add = 1 if A[i] == 1 else 0
            else:
                add = 1 if A[i] == 0 else 0
            num += add
            flip_queue.append(add)
            flip_sum += add
            if len(flip_queue) >= K:
                flip_sum -= flip_queue.pop(0)
        for j in range(n - K + 1, n):
            if flip_sum & 1:
                if A[j] == 1:
                    return -1
            elif A[j] == 0:
                return -1
            flip_queue.append(0)
            if len(flip_queue) >= K:
                flip_sum -= flip_queue.pop(0)
        return num

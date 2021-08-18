class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        interval_status = [0] * (len(A) + 1)
        counter = 0
        prev = 0
        for i in range(len(A)):
            prev ^= interval_status[i]
            curr_status = prev ^ A[i]
            if curr_status == 0:
                if i + K <= len(A):
                    interval_status[i + K] ^= 1
                    counter += 1
                    prev ^= 1

                else:
                    return -1

        return counter

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        if N <= 2:
            return N
        counters = [None] * N
        ret_val = 2
        for idx in range(N):
            if idx == 0:
                counters[idx] = Counter()
                continue
            counter = Counter()
            for prev_idx in range(idx):
                prev_counter = counters[prev_idx]
                delta = A[idx] - A[prev_idx]
                counter[delta] = max(
                    counter[delta],
                    max(prev_counter[delta] + 1, 2)
                )
                ret_val = max(ret_val, counter[delta])
                counters[idx] = counter
            # return
        return ret_val


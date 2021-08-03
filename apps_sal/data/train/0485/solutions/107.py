class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        import numpy as np
        Anp = np.array(A).astype(bool)
        idx = 0
        cnt = 0
        while idx < Anp.shape[0] - (K - 1):
            if Anp[idx]:
                idx += 1
            else:
                cnt += 1
                Anp[idx:idx + K] = ~Anp[idx:idx + K]
                idx += 1
        if np.sum(Anp[Anp.shape[0] - K:]) != K:
            return -1
        else:
            return cnt

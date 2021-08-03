class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        flips = []
        res, total = 0, 0
        for i, v in enumerate(A):
            if i < N - K + 1:
                if v == 1:
                    if total & 1:
                        total += 1
                        res += 1
                        flips.append(1)
                    else:
                        flips.append(0)
                else:
                    if total & 1:
                        flips.append(0)
                    else:
                        total += 1
                        res += 1
                        flips.append(1)
            else:
                if v == 0:
                    if not total & 1:
                        return -1
                if v == 1:
                    if total & 1:
                        return -1
            if i >= K - 1:
                total -= flips[i - K + 1]
        return res

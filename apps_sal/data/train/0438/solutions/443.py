class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        L = len(arr)
        S = 1 + 2**(L + 1)
        count = 1
        account = L // m - 1
        C = 2**m
        if m == L:
            return L

        while account:
            k = arr.pop()
            if m + 1 <= k:
                s = S >> (k - m - 1)
                if s & (2 * C - 1) == 1:
                    return L - count
                s = s >> (m + 2)
            else:
                s = (S >> k + 1) & (2 * C - 1)
            if s & (2 * C - 1) == C:
                return L - count
            S += 1 << k
            count += 1
            if arr == []:
                break
        Max = L + 1
        Min = 0
        while account == 0:
            k = arr.pop()
            if L - m >= k > Min:
                Min = k
            elif k < Max:
                Max = k
            if Max - Min == m + 1:
                return L - count
            elif Max - Min < m + 1:
                break
            count += 1
            if arr == []:
                break
        return -1

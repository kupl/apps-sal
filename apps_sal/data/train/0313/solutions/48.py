class Solution:
    def minDays(self, B: List[int], m: int, k: int) -> int:

        n = len(B)
        if m * k > n:
            return -1

        lo = min(B)
        hi = max(B) + 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            bouquets = 0
            curflowers = 0
            for i in range(n):
                if B[i] <= mi:
                    curflowers += 1
                else:
                    curflowers = 0

                if curflowers == k:
                    bouquets += 1
                    curflowers = 0
                # print(m,i,curflowers,bouquets)

                if bouquets == m:
                    # print(m,i,'here')
                    hi = mi
                    break
            if hi > mi:
                lo = mi + 1

        return lo

class Solution:

    def minOperationsMaxProfit(self, cust: List[int], b: int, r: int) -> int:
        arr = [1 * b - r, 2 * b - r, 3 * b - r, 4 * b - r]
        pos = 0
        ln = len(cust)
        for i in range(4):
            if arr[i] > 0:
                pos = i + 1
        if pos == 0:
            return -1
        prev = 0
        for i in range(ln):
            x = min(4, prev + cust[i])
            prev = prev + cust[i] - x
            cust[i] = x
        cum = 0
        for i in range(ln):
            cum += cust[i]
            cust[i] = cum * b - (i + 1) * r
        (a, b2) = (prev // 4, prev % 4)
        x = max(cust)
        y = (cum + a * 4) * b - (ln + a) * r
        z = y
        if b2:
            z = (cum + prev) * b - (ln + a + 1) * r
            if z > y:
                a += 1
        if z > x:
            if z < 1:
                return -1
            return ln + a
        if x < 1:
            return -1
        return cust.index(x) + 1

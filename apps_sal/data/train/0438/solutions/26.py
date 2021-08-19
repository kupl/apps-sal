class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        barr = [None for i in range(n + 1)]
        comp_l = defaultdict(lambda: 0)
        last = -1
        for (i, num) in enumerate(arr):
            (low, high) = (num, num)
            if num > 1 and barr[num - 1] is not None:
                (llow, lhigh) = barr[num - 1]
                comp_l[lhigh - llow + 1] -= 1
                low = llow
            if num < len(barr) - 1 and barr[num + 1] is not None:
                (rlow, rhigh) = barr[num + 1]
                comp_l[rhigh - rlow + 1] -= 1
                high = rhigh
            comp_l[high - low + 1] += 1
            barr[low] = (low, high)
            barr[high] = (low, high)
            if comp_l[m] > 0:
                last = max(last, i + 1)
        return last

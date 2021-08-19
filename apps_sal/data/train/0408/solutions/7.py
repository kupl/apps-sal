class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        (lo, hi) = (0, min(max(arr), 10 ** 5))
        while lo <= hi:
            m = (lo + hi) // 2
            s = sum((m if x > m else x for x in arr))
            if s > target:
                (lo, hi) = (lo, m - 1)
            else:
                (lo, hi) = (m + 1, hi)
        sl = sum((lo if x > lo else x for x in arr))
        sh = sum((hi if x > hi else x for x in arr))
        if abs(target - sl) >= abs(target - sh):
            return hi
        else:
            return lo

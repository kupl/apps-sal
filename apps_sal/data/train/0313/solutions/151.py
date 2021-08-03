class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        res = sys.maxsize
        while low <= high:
            med = (low + high) // 2
            i = b = 0
            while i < len(bloomDay):
                f = 0
                while i < len(bloomDay) and bloomDay[i] <= med and f < k:
                    i, f = i + 1, f + 1
                if f == k:
                    b += 1
                else:
                    i += 1
            if b < m:
                low = med + 1
            else:
                res = min(res, med)
                high = med - 1
        return res if res != sys.maxsize else -1

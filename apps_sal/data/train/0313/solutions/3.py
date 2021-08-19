class Solution:

    def minDays(self, arr: List[int], m: int, k: int) -> int:
        (l, r, n) = (0, max(arr) + 1, len(arr))
        if m * k > n:
            return -1
        while l < r:
            mid = l + (r - l) // 2
            (cnt, tmp) = (0, 0)
            for (i, v) in enumerate(arr):
                cnt = 0 if v > mid else cnt + 1
                if cnt == k:
                    tmp += 1
                    cnt = 0
                    if tmp == m:
                        break
            if tmp == m:
                r = mid
            else:
                l = mid + 1
        return l

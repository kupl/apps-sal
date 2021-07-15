class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(day):
            flowers = list(map(lambda d: d <= day, bloomDay))
            mm = 0
            kk = 0
            for f in flowers:
                if f is False:
                    kk = 0
                else:
                    kk += 1
                    if kk == k:
                        mm += 1
                        kk = 0
            return mm >= m
        days = sorted(list(set(bloomDay)))
        def binarysearch(i, j):
            if j <= i: return -1
            if j - i <= 2:
                for ii in range(i, j):
                    if check(days[ii]): return days[ii]
                return -1
            mid = (i + j) // 2
            if check(days[mid]): return binarysearch(i, mid+1)
            return binarysearch(mid+1, j)
        return binarysearch(0, len(days))

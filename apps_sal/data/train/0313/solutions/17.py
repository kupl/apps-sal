class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        def count(day):
            cnt, counter = 0, 0
            for i in range(n):
                if bloomDay[i] <= day:
                    counter += 1
                    if counter == k:
                        cnt += 1
                        counter = 0
                else:
                    counter = 0
            return cnt
        l, r = min(bloomDay), max(bloomDay)
        while l <= r:
            mid = l + (r - l) // 2
            if count(mid) < m:
                l = mid + 1
            else:
                r = mid - 1
        return l

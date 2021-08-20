class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def possible(bloomDay, days, m, k):
            bouq = 0
            curr = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= days:
                    curr += 1
                else:
                    curr = 0
                if curr == k:
                    bouq += 1
                    curr = 0
            return bouq >= m
        l = 0
        r = max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if possible(bloomDay, mid, m, k):
                r = mid
            else:
                l = mid + 1
        if possible(bloomDay, l, m, k):
            return l
        return -1

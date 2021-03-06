class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def count(d):
            total = 0
            curr = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > d:
                    curr = 0
                else:
                    curr += 1
                if curr == k:
                    total += 1
                    curr = 0
            return total
        if m * k > len(bloomDay):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            d = l + (r - l) // 2
            print(l, r, d, count(d))
            if count(d) >= m:
                r = d
            else:
                l = d + 1
        return l

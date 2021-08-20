class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def count(d):
            total = 0
            curr = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > d:
                    curr = 0
                else:
                    total += (curr + 1) // k
                    curr = (curr + 1) % k
            return total
        if m * k > len(bloomDay):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            d = l + (r - l) // 2
            if count(d) >= m:
                r = d
            else:
                l = d + 1
        return l

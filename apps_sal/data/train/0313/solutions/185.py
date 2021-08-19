class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def count(d):
            ans = 0
            curr = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= d:
                    curr += 1
                    if curr == k:
                        ans += 1
                        curr = 0
                else:
                    curr = 0
            return ans
        (l, r) = (1, max(bloomDay))
        while l < r:
            mid = (l + r) // 2
            print((l, r, mid, count(mid)))
            if count(mid) >= m:
                r = mid
            else:
                l = mid + 1
        return l

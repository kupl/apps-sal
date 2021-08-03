class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(days):
            ans = 0
            temp = k
            def func(x): return 1 if x <= days else 0
            nums = [func(i) for i in bloomDay]

            for i in nums:
                if i == 0:
                    temp = k
                else:
                    if temp == 1:
                        temp = k
                        ans += 1
                    else:
                        temp -= 1
            return ans >= m

        n = len(bloomDay)
        if n < m * k:
            return -1

        l, r = 0, max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

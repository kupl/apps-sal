class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        b = bloomDay
        if m * k > len(b):
            return -1
        else:
            def posb(c) -> bool:
                p = 0
                l = 0
                for i in range(len(b)):
                    if b[i] > c:
                        l = 0
                    else:
                        l += 1
                        if l == k:
                            p += 1
                            l = 0

                # print(p,c)

                return p >= m
            l, r = min(b), max(b)
            while l < r:
                mid = l + (r - l) // 2
                if posb(mid):
                    r = mid
                else:
                    l = mid + 1
            return l

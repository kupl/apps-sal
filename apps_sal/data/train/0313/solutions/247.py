class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay) + 1:
            return -1
        pos = False

        def possible(mid):
            a, curr = 0, 0
            for bloom in bloomDay:
                if bloom > mid:
                    a = 0
                else:
                    a += 1
                    if a == k:
                        a = 0
                        curr += 1
            if curr >= m:
                return True
            else:
                return False

        left, right = min(bloomDay), max(bloomDay)
        while(left < right):
            mid = left + (right - left) // 2
            if possible(mid):
                pos = True
                right = mid
            else:
                left = mid + 1

        if possible(left):
            return left

        else:
            return -1

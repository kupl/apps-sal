class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        max_, min_ = max(bloomDay), min(bloomDay)

        def check(day):
            m_done = 0
            cont_count = 0
            for x in bloomDay:
                if x <= day:
                    cont_count += 1
                    if cont_count == k:
                        m_done += 1
                        cont_count = 0
                else:
                    cont_count = 0
            if m_done < m:
                return False
            return True

        left = min_ - 1
        right = max_

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

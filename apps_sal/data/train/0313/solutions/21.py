class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(days_cand):
            nonlocal bloomDay
            nonlocal m
            nonlocal k
            nonlocal res

            bukets = 0
            flowers_per_cur_bucket = 0

            for i in range(len(bloomDay)):
                today = bloomDay[i]
                if today <= days_cand:
                    flowers_per_cur_bucket += 1
                    if flowers_per_cur_bucket == k:
                        bukets += 1
                        flowers_per_cur_bucket = 0
                        if bukets == m:
                            res = min(res, days_cand)
                            return True
                    pass
                else:
                    flowers_per_cur_bucket = 0
                    pass
            return False

        res = float('inf')
        left = min(bloomDay)
        right = max(bloomDay) + 1

        while left < right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        if res < float('inf'):
            return left
        return -1

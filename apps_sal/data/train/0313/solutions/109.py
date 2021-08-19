class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay) + 1

        def feasible(val):
            flowers = [True if val >= d else False for d in bloomDay]
            count = 0
            total = m
            while flowers:
                if flowers.pop():
                    count += 1
                else:
                    count = 0
                if count >= k:
                    total -= 1
                    count -= k
                    if total == -1:
                        break
            return total <= 0
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        if low == max(bloomDay) + 1:
            return -1
        else:
            return low

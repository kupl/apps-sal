class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) // k < m:
            return -1
        low, high = min(bloomDay), max(bloomDay)

        def valid(days):
            start = 0
            count = 0
            for i, val in enumerate(bloomDay):
                if val <= days:
                    if i - start + 1 >= k:
                        count += 1
                        start = i + 1
                else:
                    start = i + 1

            return count >= m

        while low < high:
            days = (low + high) // 2

            if valid(days):
                high = days
            else:
                low = days + 1

        return low

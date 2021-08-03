class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        tmp = sorted(list(set(bloomDay)))
        low = 0
        high = len(tmp) - 1

        def feasible(val):
            count = 0
            total = m

            for day in bloomDay:
                if val >= day:
                    count += 1

                    if count == k:
                        total -= 1
                        count = 0

                        if total == -1:
                            break

                else:
                    count = 0

            return total <= 0

        while low < high:
            mid = (low + high) // 2
            val = tmp[mid]

            if feasible(val):
                high = mid
            else:
                low = mid + 1

        return tmp[low]

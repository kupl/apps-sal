from itertools import groupby


class Solution:

    def minDays(self, b: List[int], m: int, k: int) -> int:

        def is_possible(arr, min_day):
            after_days = [1 if min_day >= d else 0 for d in b]
            cont_days = sum([len(list(g)) // k for (num, g) in groupby(after_days) if num == 1])
            return cont_days >= m
        if m * k > len(b):
            print(-1)
            return -1
        else:
            (left, right) = (min(b), max(b))
            while left < right:
                mid = left + (right - left) // 2
                if is_possible(b, mid):
                    right = mid
                else:
                    left = mid + 1
            print(left)
            return left

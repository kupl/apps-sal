import heapq


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def is_valid(mid):
            (count, size) = (0, 0)
            for (i, v) in enumerate(bloomDay):
                size = size + 1 if v <= mid else 0
                if size == k:
                    size = 0
                    count += 1
                if count == m:
                    return True
            return False
        (left, right) = (float('inf'), float('-inf'))
        for (i, v) in enumerate(bloomDay):
            left = min(left, v)
            right = max(right, v)
        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if left != float('-inf') else -1

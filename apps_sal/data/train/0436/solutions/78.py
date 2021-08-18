import math
from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        if n < 2:
            return n
        queue = deque()
        running_count = n
        min_days = 0
        queue.append((min_days, n))
        seen = set()
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                local_min, local_n = queue.popleft()
                seen.add(local_n)
                if local_n < 0:
                    continue
                if local_n == 0:
                    return local_min

                if local_n % 2 == 0 and local_n - local_n // 2 not in seen:
                    queue.append((local_min + 1, (local_n - local_n // 2)))
                if local_n % 3 == 0 and local_n - 2 * (local_n // 3) not in seen:
                    queue.append((local_min + 1, (local_n - 2 * (local_n // 3))))
                queue.append((local_min + 1, local_n - 1))
        return min_days

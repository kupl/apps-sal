class Solution:
    def minDays(self, n: int) -> int:
        queue = [[n, 0]]
        seen = set()
        for i, d in queue:
            if i == 0:
                return d
            seen.add(i)
            if i % 3 == 0 and i // 3 not in seen:
                queue.append([i // 3, d + 1])
            if i % 2 == 0 and i // 2 not in seen:
                queue.append([i // 2, d + 1])
            if i - 1 not in seen:
                queue.append([i - 1, d + 1])

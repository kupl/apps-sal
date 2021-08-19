from queue import Queue


class Solution:

    def minDays(self, n: int) -> int:
        q = Queue()
        seen = set()
        q.put((n, 0))
        seen.add(n)
        while not q.empty():
            (cur, days) = q.get()
            if cur == 1:
                return days + 1
            q.put((cur - 1, days + 1))
            seen.add(cur - 1)
            if cur % 2 == 0 and cur // 2 not in seen:
                q.put((cur // 2, days + 1))
                seen.add(cur // 2)
            if cur % 3 == 0 and cur // 3 not in seen:
                q.put((cur // 3, days + 1))
                seen.add(cur // 3)

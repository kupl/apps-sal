from queue import Queue


class Solution:

    def minDays(self, n: int) -> int:
        q = Queue()
        q.put((n, 0))
        visited = set()
        num = n
        while num != 0:
            (num, days) = q.get()
            if num not in visited:
                visited.add(num)
                if num % 3 == 0:
                    q.put((num // 3, days + 1))
                if num % 2 == 0:
                    q.put((num // 2, days + 1))
                q.put((num - 1, days + 1))
        return days

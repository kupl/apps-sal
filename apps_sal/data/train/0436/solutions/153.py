class Solution:

    def minDays(self, n: int) -> int:
        q = collections.deque()
        days = 0
        q.append(n)
        seen = set()
        seen.add(n)
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == 0:
                    return days
                if cur - 1 not in seen:
                    seen.add(cur - 1)
                    q.append(cur - 1)
                if cur % 2 == 0 and cur % 2 not in seen:
                    q.append(cur // 2)
                if cur % 3 == 0 and cur % 3 not in seen:
                    q.append(cur // 3)
            days += 1
        return -1

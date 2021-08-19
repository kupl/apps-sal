class Solution:

    def minDays(self, n: int) -> int:
        q = deque()
        q.append(n)
        days = 0
        seen = set()
        while q:
            days += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == 1:
                    return days
                if node % 3 == 0 and node // 3 not in seen:
                    q.append(node // 3)
                    seen.add(node // 3)
                if node % 2 == 0 and node // 2 not in seen:
                    q.append(node // 2)
                    seen.add(node // 2)
                if node - 1 not in seen:
                    q.append(node - 1)
                    seen.add(node - 1)

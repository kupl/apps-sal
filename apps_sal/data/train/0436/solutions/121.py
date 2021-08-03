class Solution:
    def minDays(self, n: int) -> int:
        q = deque([n])
        level = 0
        visited = set()
        while q:
            # print(q)
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur == 0:
                    return level
                if cur % 2 == 0 and cur - cur // 2 not in visited:
                    visited.add(cur - cur // 2)
                    q.append(cur - cur // 2)
                if cur % 3 == 0 and cur - 2 * cur // 3 not in visited:
                    visited.add(cur - 2 * cur // 3)
                    q.append(cur - 2 * cur // 3)
                if cur - 1 not in visited:
                    visited.add(cur - 1)
                    q.append(cur - 1)
            level += 1

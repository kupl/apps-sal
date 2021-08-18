

class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        visited = set([n])
        q = collections.deque([n])
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur == 0:
                    return ans
                if cur - 1 not in visited:
                    visited.add(cur - 1)
                    q.append(cur - 1)
                if cur % 2 == 0 and cur // 2 not in visited:
                    visited.add(cur // 2)
                    q.append(cur // 2)
                if cur % 3 == 0 and cur // 3 not in visited:
                    visited.add(cur // 3)
                    q.append(cur // 3)
            ans += 1
        return -1

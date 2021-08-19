class Solution:

    def minDays(self, n: int) -> int:
        dq = deque([(0, n)])
        res = 0
        seen = set()
        while dq:
            (layer, num) = dq.popleft()
            if num in seen:
                continue
            else:
                seen.add(num)
            if num == 0:
                return layer
            if num % 3 == 0:
                dq.append((layer + 1, num / 3))
            if num % 2 == 0:
                dq.append((layer + 1, num / 2))
            dq.append((layer + 1, num - 1))
        return 0

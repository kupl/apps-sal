class Solution:

    def minDays(self, n: int) -> int:
        visited = set()
        days = -1
        q = [n]
        while q:
            days += 1
            nxt_q = []
            while q:
                cur = q.pop()
                visited.add(cur)
                if cur == 0:
                    return days
                nxt_q.append(cur - 1)
                if cur % 2 == 0:
                    if cur // 2 not in visited:
                        nxt_q.append(cur // 2)
                if cur % 3 == 0:
                    if cur // 3 not in visited:
                        nxt_q.append(cur // 3)
            q = nxt_q
        return n

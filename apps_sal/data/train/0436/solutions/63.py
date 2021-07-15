class Solution:
    def minDays(self, n: int) -> int:
        days = 0
        tosee = deque([n])
        seen = set([])
        while tosee:
            s = len(tosee)
            while s:
                s -= 1
                cur = tosee.popleft()
                seen.add(cur)
                if cur == 0:
                    return days
                if cur % 2 == 0 and cur // 2 not in seen:
                    tosee.append(cur // 2)
                if cur % 3 == 0 and cur // 3 not in seen:
                    tosee.append(cur // 3)
                if cur - 1 not in seen:
                    tosee.append(cur - 1)
            days += 1
        return -1

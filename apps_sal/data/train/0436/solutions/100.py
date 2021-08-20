from collections import deque


class Solution:

    def minDays(self, n: int) -> int:
        d = {}
        q = deque([n])
        d[n] = 0
        while q and 0 not in d:
            item = q.popleft()
            day = d[item] + 1
            temp = [item - 1]
            if item % 2 == 0:
                temp.append(item // 2)
            if item % 3 == 0:
                temp.append(item // 3)
            for i in temp:
                if i not in d:
                    d[i] = day
                    q.append(i)
        return d[0]

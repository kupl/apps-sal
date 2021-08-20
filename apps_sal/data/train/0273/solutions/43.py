from collections import deque


class Solution:

    def racecar(self, target: int) -> int:
        dic = {}
        qu = deque([(0, 1)])
        dic[0, 1] = 0
        while qu:
            front = qu.popleft()
            (pos, spd) = front
            if pos == target:
                return dic[front]
            speedup = (pos + spd, spd * 2)
            if speedup not in dic:
                qu.append(speedup)
                dic[speedup] = dic[front] + 1
            fwd2bwd = (pos, -1)
            if spd > 0 and fwd2bwd not in dic:
                qu.append(fwd2bwd)
                dic[fwd2bwd] = dic[front] + 1
            bwd2fwd = (pos, 1)
            if spd < 0 and (pos, 1) not in dic:
                qu.append((pos, 1))
                dic[bwd2fwd] = dic[front] + 1

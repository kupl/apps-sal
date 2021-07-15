class Solution:
    def racecar(self, target):
        target *= -1
        q, used = [(0, 0, -1)], {(0, -1)}
        while q:
            cnt, pos, speed = heapq.heappop(q)
            if pos == target:
                return cnt
            elif pos > 20000 or -20000 > pos:
                continue
            if (pos + speed, speed * 2) not in used:
                heapq.heappush(q, (cnt + 1, pos + speed, speed * 2))
                used.add((pos + speed, speed * 2))
            if speed < 0 and (pos, 1) not in used:
                heapq.heappush(q, (cnt + 1, pos, 1))
                used.add((pos, 1))
            elif speed > 0 and (pos, -1) not in used:
                heapq.heappush(q, (cnt + 1, pos, -1))
                used.add((pos, -1))

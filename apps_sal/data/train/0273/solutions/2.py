class Solution:

    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])
        encountered = set()
        while q:
            (pos, spd, length) = q.popleft()
            if (pos, spd) in encountered:
                continue
            else:
                encountered.add((pos, spd))
            if pos == target:
                return length
            if (pos + spd, spd * 2) not in encountered:
                if abs(pos + spd) <= 2 * target + 1:
                    q.append((pos + spd, spd * 2, length + 1))
            revSpd = -1 if spd > 0 else 1
            if (pos, revSpd) not in encountered:
                q.append((pos, revSpd, length + 1))
        return -1

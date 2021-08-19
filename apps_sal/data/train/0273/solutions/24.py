import collections


class Solution:

    def racecar(self, target: int) -> int:
        q = collections.deque([(0, 0, 1)])
        while q:
            (move, pos, vel) = q.popleft()
            if pos == target:
                return move
            q.append((move + 1, pos + vel, vel * 2))
            if pos > target and vel > 0 or (pos < target and vel < 0) or (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                q.append((move + 1, pos, -1 if vel > 0 else 1))

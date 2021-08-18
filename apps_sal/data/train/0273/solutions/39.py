class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        q = {(0, 1)}
        visited = {(0, 1)}
        steps = -1
        while q:
            steps += 1
            next_q = set()
            for pos, speed in q:
                if pos == target:
                    return steps
                state_A = (pos + speed, speed * 2)
                if state_A not in visited:
                    visited.add(state_A)
                    next_q.add(state_A)
                state_R = (pos, -1 if speed > 0 else 1)
                if state_R not in visited:
                    visited.add(state_R)
                    next_q.add(state_R)
            q = next_q
        return steps

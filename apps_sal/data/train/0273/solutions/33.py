class Solution:
    def racecar(self, target: int) -> int:
        visited = {(0, 1)}
        queue = collections.deque()
        queue.append((0, 1))
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                s, v = queue.popleft()
                if s == target:
                    return steps
                cur_s = s + v
                cur_v = v * 2
                if (cur_s, cur_v) not in visited:
                    queue.append((cur_s, cur_v))
                    visited.add((cur_s, cur_v))
                cur_s = s
                cur_v = -1 if v > 0 else 1
                if (cur_s, cur_v) not in visited:
                    queue.append((cur_s, cur_v))
                    visited.add((cur_s, cur_v))
            steps += 1

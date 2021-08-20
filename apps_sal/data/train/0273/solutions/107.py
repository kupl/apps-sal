class Solution:

    def racecar(self, target: int) -> int:
        queue = [(0, 1)]
        visited = set((0, 1))
        step = 0
        q = 0
        while len(queue) > q:
            step += 1
            size = len(queue) - q
            for _ in range(size):
                (x, v) = queue[q]
                q += 1
                x_ = x + v
                v_ = v * 2
                if (x_, v_) not in visited and abs(x_) < 2 * target:
                    queue.append((x_, v_))
                    visited.add((x_, v_))
                    if x_ == target:
                        return step
                x_ = x
                if v > 0:
                    v_ = -1
                else:
                    v_ = 1
                if (x_, v_) not in visited and abs(x_) < 2 * target:
                    queue.append((x_, v_))
                    visited.add((x_, v_))
                    if x_ == target:
                        return step

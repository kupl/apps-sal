from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set((0, 1))
        level = 0
        while queue:
            num = len(queue)
            for _ in range(num):
                cur_pos, cur_speed = queue.popleft()
                if cur_pos == target:
                    return level
                nex_acc = (cur_pos + cur_speed, cur_speed * 2)
                if nex_acc not in visited and 0 < nex_acc[0] < target * 2:
                    queue.append(nex_acc)
                    visited.add(nex_acc)
                nex_rev = (cur_pos, -1 if cur_speed > 0 else 1)
                if nex_rev not in visited and 0 < nex_rev[0] < target * 2:
                    queue.append(nex_rev)
                    visited.add(nex_rev)
            level += 1
        return -1

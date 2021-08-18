class Solution:
    def racecar(self, target: int) -> int:
        nodes = [(0, 1)]
        seen, length = set([(0, 1), (0, -1)]), 0
        while nodes:
            new_nodes = []
            for pos, speed in nodes:
                if pos == target:
                    return length
                for new_pos, new_speed in [
                    (pos + speed, speed * 2),
                    (pos, -1 if speed > 0 else 1),
                ]:
                    if abs(new_speed) > 2 * target or abs(new_pos) > 2 * target:
                        continue
                    if (new_pos, new_speed) not in seen:
                        seen.add((new_pos, new_speed))
                        new_nodes.append((new_pos, new_speed))
            length += 1
            nodes = new_nodes
        return -1

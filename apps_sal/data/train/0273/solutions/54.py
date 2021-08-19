class Solution:

    def racecar(self, target: int) -> int:
        queue = [[(0, 1)]]
        visited = {(0, 1)}
        seq = 0
        while queue:
            curLevel = queue.pop()
            newLevel = []
            for (pos, speed) in curLevel:
                if pos == target:
                    return seq
                for (newPos, newSpeed) in [(pos + speed, speed * 2), (pos, -1 if speed > 0 else 1)]:
                    if (newPos, newSpeed) not in visited:
                        visited.add((newPos, newSpeed))
                        newLevel.append((newPos, newSpeed))
            if newLevel:
                queue.append(newLevel)
                seq += 1
        return -1

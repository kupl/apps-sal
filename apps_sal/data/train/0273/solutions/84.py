class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque()
        visited = set()
        queue.append((0, 1, 0))
        visited.add((0, 1))
        
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            
            next_pos = pos + speed
            next_speed = speed * 2
            if (next_pos, next_speed) not in visited and next_pos < 2 * target and next_pos > 0:
                queue.append((next_pos, next_speed, steps + 1))
                visited.add((next_pos, next_speed))
            
            next_pos = pos
            next_speed = -1 if speed > 0 else 1
            if (next_pos, next_speed) not in visited and next_pos < 2 * target and next_pos > 0:
                queue.append((next_pos, next_speed, steps + 1))
                visited.add((next_pos, next_speed))
        
        return -1


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        seen = {(0, 1)}
        while queue:
            pos, speed, cost = queue.popleft()
            if pos == target:
                return cost
            
            # A
            new_pos, new_speed = pos + speed, speed * 2
            if new_pos > 0 and (new_pos, new_speed) not in seen:
                seen.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, cost + 1)) # A
                
            # R
            reverse_speed = -1 if speed > 0 else 1
            if (pos, reverse_speed) not in seen:
                seen.add((pos, reverse_speed))
                queue.append((pos, reverse_speed, cost + 1))


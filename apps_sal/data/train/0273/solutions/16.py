class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0

        pq = [(0, 0, -1)]  # steps, pos, speed
        visited = set([(0, -1)])

        while pq:
            steps, pos, speed = heapq.heappop(pq)

            next_steps, next_pos, next_speed = steps + 1, pos + speed, speed * 2

            if -next_pos == target:
                return next_steps

            if -2 * target < -next_pos < 2 * target and -2 * target < -next_speed < 2 * target and not (next_pos, next_speed) in visited:
                # if -next_pos < 2 * target and -next_speed < 2 * target and not (next_pos, next_speed) in visited:
                heapq.heappush(pq, (next_steps, next_pos, next_speed))
                visited.add((next_pos, next_speed))

            if speed > 0 and not (pos, -1) in visited:
                heapq.heappush(pq, (next_steps, pos, -1))
                visited.add((pos, -1))
            elif speed < 0 and not (pos, 1) in visited:
                heapq.heappush(pq, (next_steps, pos, 1))
                visited.add((pos, 1))
        return -1

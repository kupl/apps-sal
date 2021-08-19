class Solution:

    def racecar(self, target: int) -> int:
        record = collections.defaultdict(int)
        cur = (0, 1)
        queue = collections.deque()
        queue.append(cur)
        record[cur] = 0
        while True:
            for _ in range(len(queue)):
                (pos, speed) = queue.popleft()
                step = record[pos, speed]
                if pos == target:
                    return step
                if pos + speed == target:
                    return 1 + step
                s1 = (pos + speed, speed * 2)
                s2 = (pos, -1) if speed > 0 else (pos, 1)
                if s1 not in record:
                    queue.append(s1)
                    record[s1] = step + 1
                if s2 not in record:
                    queue.append(s2)
                    record[s2] = step + 1
        return -1

class Solution:
    def racecar(self, target: int) -> int:
        stack = collections.deque([(0, 1, 0)])
        seen = set([(0, 1)])
        while stack:
            pos, speed, steps = stack.popleft()
            if pos == target:
                return steps

            new = (pos + speed, speed * 2)
            if new not in seen:
                seen.add(new)
                stack.append((new[0], new[1], steps + 1))

            new = (pos, -1 if speed > 0 else 1)
            if new not in seen:
                seen.add(new)
                stack.append((new[0], new[1], steps + 1))

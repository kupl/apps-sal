class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        dists = {(0, 1): 0}
        while queue:
            x, v = queue.popleft()
            d = dists[(x, v)]
            if x + v == target:
                return d + 1
            y, w = x + v, v << 1
            if (y, w) not in dists:
                dists[(y, w)] = d + 1
                queue.append((y, w))
            opv = -1 if v > 0 else 1
            if (x, opv) not in dists:
                dists[(x, opv)] = d + 1
                queue.append((x, opv))

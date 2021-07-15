class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        return self.helper(blocked, source, target) and self.helper(blocked, target, source)
    def helper(self, blocked, source, target):
        if not blocked: return True
        dq = collections.deque([tuple(source)])
        l = len(blocked)
        seen = {tuple(source)}
        blocked = set(map(tuple, blocked))
        while dq:
            sz = len(dq)
            for _ in range(sz):
                x, y = dq.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < 10 ** 6 and 0 <= yy < 10 ** 6 and (xx, yy) not in seen and (xx, yy) not in blocked:
                        seen.add((xx, yy))
                        dq.append((xx, yy))
                        # the maximum area covered by blocks will be an isosceles right triangle with area less than l * l // 2
                        # if we can cover more cells than l * l // 2, we will be bound to break the block
                        if (xx, yy) == tuple(target) or len(seen) >= l * l // 2: return True
        return False

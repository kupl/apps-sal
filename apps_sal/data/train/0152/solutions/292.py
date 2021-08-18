class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def is_feasible(force):
            count = 1
            cur = position[0]
            for i in range(1, n):
                if position[i] - cur >= force:
                    count += 1
                    cur = position[i]
            return count >= m

        l = 1
        r = position[-1] - position[0] + 1
        while l < r:
            med = (l + r) // 2
            if is_feasible(med):
                l = med + 1
            else:
                r = med
        return l - 1

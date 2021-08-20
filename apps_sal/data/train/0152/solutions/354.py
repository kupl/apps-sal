class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def feasible(dist, m):
            pre_pos = position[0]
            placed = 1
            for i in range(1, len(position)):
                if position[i] - pre_pos >= dist:
                    placed += 1
                    if placed >= m:
                        return True
                    pre_pos = position[i]
            return False
        l = 1
        r = position[-1] - position[0]
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid, m):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1

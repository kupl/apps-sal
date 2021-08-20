class Solution:

    def feasible(self, d, m):
        last_pos = self.position[0]
        i = 1
        num_placed = 1
        while num_placed < m and i < self.plen:
            if self.position[i] - last_pos >= d:
                last_pos = self.position[i]
                num_placed += 1
            i += 1
        return num_placed == m

    def maxDistance(self, position: List[int], m: int) -> int:
        self.position = position
        self.plen = len(self.position)
        self.position.sort()
        left = 1
        right = self.position[-1] - self.position[0] + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.feasible(mid, m):
                left = mid
            else:
                right = mid
        return left

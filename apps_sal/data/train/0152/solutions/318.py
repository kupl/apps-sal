class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo = 1
        hi = position[-1]
        while lo < hi:
            dist = (hi + lo) // 2 + 1
            if self.maxBalls(position, dist) >= m:
                lo = dist
            else:
                hi = dist - 1
        return lo

    def maxBalls(self, sorted_position: List[int], distance: int) -> int:
        l_ind = 0
        r_ind = 1
        count = 1
        while r_ind < len(sorted_position):
            if sorted_position[r_ind] - sorted_position[l_ind] >= distance:
                count += 1
                l_ind = r_ind
            r_ind += 1
        return count

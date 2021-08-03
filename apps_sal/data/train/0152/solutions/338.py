class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position = sorted(position)
        m_vals = []
        distance = position[-1] - position[0]

        def works(min_dist):
            i = 1
            count = 1
            prev = 0
            while count < m and i < n:
                if position[i] - position[prev] >= min_dist:
                    count += 1
                    prev = i
                i += 1
            return count == m

        low = 0
        high = 1 << 32
        while high - low > 1:
            mid = (low + high) // 2
            if works(mid):
                low = mid
            else:
                high = mid - 1
        if works(high):
            return high
        return low

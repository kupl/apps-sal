class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def feasible(min_req_dist, b):
            i = 0
            prev_pos = None
            while i < len(position) and b > 0:
                if prev_pos == None or position[i] - prev_pos >= min_req_dist:
                    b -= 1
                    prev_pos = position[i]
                i += 1
            return b == 0

        position.sort()
        low = 1
        high = position[-1]
        while low < high:
            mid = (low + high) // 2 + 1
            if feasible(mid, m):
                low = mid
            else:
                high = mid - 1
        return low

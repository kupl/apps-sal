class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def find_distance(mid_pos):

            count = 1
            pre = position[0]
            for i in range(1, len(position)):
                distance = position[i] - pre
                if distance >= mid_pos:
                    count += 1
                    pre = position[i]
            return count

        position = sorted(position)
        lo = 0
        hi = position[-1]
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if find_distance(mid) >= m:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def canPut(distance: int) -> bool:
            count = 1
            curr = position[0]
            for pos in position[1:]:
                if pos >= curr + distance:
                    count += 1
                    curr = pos
                    if count >= m:
                        return True
            return False

        position.sort()
        lo, hi = 1, position[-1] - position[0]
        max_distance = lo

        while lo <= hi:
            mi = (lo + hi) // 2
            if canPut(mi):
                lo = mi + 1
                max_distance = max(max_distance, mi)
            else:
                hi = mi - 1

        return max_distance

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def checkForce(force, positions, m):
            i, prev = 1, positions[0]
            while m > 0 and i < len(positions):
                while positions[i] - force < prev:
                    i += 1
                    if i >= len(positions):
                        return False
                prev = positions[i]
                m -= 1
                i += 1
            return m <= 0

        l, r = 0, position[-1]
        while l < r:
            mid = r - (r - l) // 2
            # force is acceptable, let's see if we can achieve a higher force
            if checkForce(mid, position, m - 1):
                l = mid
            else:
                r = mid - 1
        return l

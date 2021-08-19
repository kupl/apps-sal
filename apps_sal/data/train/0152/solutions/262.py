class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position = sorted(position)
        lo = 1
        hi = position[-1] - position[0]

        while lo < hi:

            mid = (lo + hi + 1) // 2

            # count number of balls that can be placed if distance at least mid
            ind1 = 0
            ind2 = 1
            count = 1
            while ind2 < len(position) and count < m:

                if position[ind2] - position[ind1] >= mid:
                    count += 1
                    ind1 = ind2

                ind2 += 1

            if count >= m:
                lo = mid
            else:
                hi = mid - 1

        return lo

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        minp, maxp = min(position), max(position)
        if m == 2:
            return maxp - minp

        position.sort()

        def valid(i):

            count = 1
            ending = position[0]
            for j in range(1, len(position)):
                if position[j] >= ending + i:
                    count += 1
                    ending = position[j]

            return True if count >= m else False

        left, right = 0, maxp - minp + 1

        while right - left > 1:
            mid = left + (right - left) // 2
            if valid(mid):
                left = mid
            else:
                right = mid
        return left

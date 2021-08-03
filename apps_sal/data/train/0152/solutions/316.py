class Solution:

    def check(self, position, m, mid):

        lastpos = position[0]
        rem = m - 1

        i = 1

        while i < len(position) and rem:

            if position[i] - lastpos < mid:
                i += 1

            else:
                rem -= 1
                lastpos = position[i]

        return rem == 0

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        low = 1
        high = 10**9

        while low < high:
            mid = low + (high - low) // 2

            if self.check(position, m, mid):
                low = mid + 1

            else:
                high = mid

        return low - 1

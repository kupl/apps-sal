class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()

        def ispossible(f: int) -> bool:
            Count, pos = 1, 0

            for i in range(1, len(position)):

                if position[i] - position[pos] >= f:
                    pos = i
                    Count += 1

            return bool(Count >= m)

        start, end = 1, position[-1] - position[0]

        while start < end:

            mid = (start + end) // 2
            if ispossible(mid) and not ispossible(mid + 1):
                return mid
            elif ispossible(mid):
                start = mid + 1
            else:
                end = mid - 1

        return start

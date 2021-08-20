class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        result = 0

        def check(x) -> bool:
            nonlocal position, m
            last = position[0]
            placed = 1
            for pos in position:
                if pos - last >= x:
                    placed += 1
                    if placed >= m:
                        return True
                    last = pos
            return False
        first = 0
        last = int(ceil((position[-1] - position[0]) / (m - 1)))
        while first < last:
            mid = (first + last + 1) // 2
            if check(mid):
                result = mid
                first = mid
            else:
                last = mid - 1
        return first

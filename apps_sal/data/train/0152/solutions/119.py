from array import array


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        position = array('i', position)
        high = position[-1] - position[0]
        low = high
        for i in range(1, len(position)):
            low = min(position[i] - position[i - 1], low)

        def count(step):
            c = 1
            pivot = 0
            for i in range(1, len(position)):
                if step <= (position[i] - position[pivot]):
                    c += 1
                    pivot = i
            return c
        res = None
        while low <= high:
            mid = low + (high - low) // 2
            num = count(mid)
            if num >= m:
                res = mid
                low = mid + 1
            if num < m:
                high = mid - 1
        return res

class Solution:

    def verify(self, position: List[int], dis: int, balls: int) -> bool:
        result = True
        start = position[0]
        cur = 1
        counter = 1
        while cur < len(position):
            if position[cur] >= start + dis:
                start = position[cur]
                counter += 1
                if counter >= balls:
                    return True
            cur += 1

        return False

    def maxDistance(self, position: List[int], m: int) -> int:

        result = 0
        position = sorted(position)
        minvalue = sys.maxsize
        maxvalue = -sys.maxsize
        for value in position:
            minvalue = min(minvalue, value)
            maxvalue = max(maxvalue, value)

        left = 1
        right = maxvalue - minvalue
        while left <= right:
            mid = left + (right - left) // 2
            checked = self.verify(position, mid, m)
            if checked:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return result

class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        (l, r) = (1, position[len(position) - 1] - position[0])

        def is_doable(gap):
            (count, pre) = (0, position[0] - 2 * gap)
            for element in position:
                if element - pre >= gap:
                    pre = element
                    count += 1
                    if count == m:
                        return True
            return False
        while True:
            mid = (l + r) // 2
            if is_doable(mid):
                if mid == position[len(position) - 1] - position[0]:
                    return mid
                elif is_doable(mid + 1):
                    l = mid + 1
                else:
                    return mid
            else:
                r = mid - 1

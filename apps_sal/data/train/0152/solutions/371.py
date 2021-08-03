class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]

        else:
            maxd = position[-1] // (m - 1)

        start = 1
        end = maxd

        while start < end:
            middle = (start + end) // 2
            result = self.is_satisfy(position, middle, m)
            if result:
                if start == middle:
                    result2 = self.is_satisfy(position, middle + 1, m)
                    if result2:
                        return middle + 1
                    else:
                        return middle
                start = middle
            else:
                end = middle - 1

        return start

    def is_satisfy(self, position, maxd, m):
        pre_postion = position[0]
        index = 1
        left_count = m - 1

        pcount = len(position)

        while index < pcount:
            if position[index] - pre_postion < maxd:
                index += 1
                continue

            left_count -= 1
            if left_count == 0:
                return True

            pre_postion = position[index]
            index += 1

        return False

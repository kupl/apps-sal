
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m

        result = -1
        length = []
        for i in range(len(arr) + 2):
            length.append(0)

        for index, value in enumerate(arr):
            left = length[value - 1]
            right = length[value + 1]
            if left == m or right == m:
                result = index

            length[value - left] = left + right + 1
            length[value + right] = left + right + 1
            pass

        return result

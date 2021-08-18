import bisect


class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        i, j = 0, max(arr)
        while i <= j:
            mid = (i + j) // 2
            dist = sum(v if v < mid else mid for v in arr)
            if dist == target:
                return mid
            elif dist < target:
                i = mid + 1
            else:
                j = mid - 1

        disti = sum(v if v < i else i for v in arr)
        disti_1 = sum(v if v < (i - 1) else (i - 1) for v in arr)
        print((disti, disti_1, i, j))

        return i if abs(disti - target) < abs(disti_1 - target) else (i - 1)

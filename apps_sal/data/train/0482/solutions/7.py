class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0

        while (len(arr) > 1):

            mid = arr.index(min(arr))

            res += min(arr[mid - 1:mid] + arr[mid + 1:mid + 2]) * arr.pop(mid)

        return res

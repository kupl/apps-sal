class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            v = min(arr)
            idx = arr.index(v)
            res += min(arr[idx - 1:idx] + arr[idx + 1:idx + 2]) * arr[idx]
            arr.pop(idx)

        return res

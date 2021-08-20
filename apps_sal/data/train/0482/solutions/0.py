class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
        res = []
        while len(arr) > 1:
            temp_res = []
            temp_res = [arr[i] * arr[i + 1] for i in range(len(arr) - 1)]
            idx = temp_res.index(min(temp_res))
            res.append(temp_res[idx])
            arr.pop(idx if arr[idx] < arr[idx + 1] else idx + 1)
        return sum(res)

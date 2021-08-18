class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodel, delected = 0, 0
        res = float('-inf')
        for num in arr:
            delected = max(nodel, delected + num)
            nodel = max(nodel, 0) + num
            res = max(nodel, delected, res)
        return res

    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        nodel, delected = arr[0], 0
        res = arr[0]
        for num in arr[1:]:
            delected = max(nodel, delected + num)
            nodel = max(nodel, 0) + num
            res = max(nodel, delected, res)
        return res

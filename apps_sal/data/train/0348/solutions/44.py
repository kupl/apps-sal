class Solution:

    def maximumSum(self, arr: List[int]) -> int:
        if not arr:
            return 0
        max_del = arr[0]
        max_no_del = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            max_del = max(max_del + arr[i], max_no_del, arr[i])
            max_no_del = max(max_no_del + arr[i], arr[i])
            res = max(res, max_del)
        return res

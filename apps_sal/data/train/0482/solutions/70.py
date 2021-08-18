class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        def to_remove():
            cur_min = arr[0] * arr[1]
            res = 0 if arr[0] < arr[1] else 1
            for i in range(len(arr) - 1):
                if arr[i] * arr[i + 1] < cur_min:
                    cur_min = arr[i] * arr[i + 1]
                    res = i if arr[i] < arr[i + 1] else i + 1
            return res
        res = 0
        while len(arr) > 1:
            i = to_remove()
            res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)

        return res

        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)
            print(res, arr)
        return res

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            mini_idx = arr.index(min(arr))
            if 0 < mini_idx < len(arr) - 1:
                res += min(arr[mini_idx - 1], arr[mini_idx + 1]) * arr[mini_idx]
            else:
                if mini_idx == 0:
                    adj_idx = 1
                else:
                    adj_idx = mini_idx - 1
                res += arr[adj_idx] * arr[mini_idx]
            arr.pop(mini_idx)
            # print(arr)
            # print(res)
        return res

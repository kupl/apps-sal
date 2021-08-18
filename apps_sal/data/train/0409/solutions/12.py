class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if sorted(arr)[0] >= 0:
            return sum(arr) * k % (10**9 + 7)
        if sorted(arr)[-1] <= 0:
            return 0
        if k > 1:
            arr = arr + [max(0, sum(arr) * (k - 2))] + arr
        temp, res = 0, 0
        for i in range(len(arr)):
            temp += arr[i]
            res = max(res, temp)
            if temp < 0:
                temp = 0
        return res % (10**9 + 7)

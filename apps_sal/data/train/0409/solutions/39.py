class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        c = sum(arr)
        out = 0
        straight_sum = arr[:]
        back_sum = arr[:]
        s = 0
        for i in range(1, len(straight_sum)):
            straight_sum[i] = max(straight_sum[i], straight_sum[i - 1] + straight_sum[i])
        out = max(max(straight_sum), out)
        for i in range(len(arr)):
            out = max(out, arr[i])
            s += arr[i]
            straight_sum[i] = s
        s = 0
        for i in range(len(arr) - 1, -1, -1):
            s += arr[i]
            back_sum[i] = s
        if k == 1:
            out = max(out, max(straight_sum), max(back_sum))
            return out
        if k > 2:
            out = max(out, max(straight_sum) + max(back_sum) + c * (k - 2))
        out = max(max(straight_sum) + max(back_sum), out)
        return out % (10 ** 9 + 7)

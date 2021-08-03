class Solution:
    def maxSumTwoNoOverlap(self, arr: List[int], L: int, M: int) -> int:
        Lsum = [0] * len(arr)
        Msum = [0] * len(arr)

        def makeWindow(arr, res, size):
            window = 0
            for i in range(0, size):
                window += arr[i]
            res[i] = window

            for i in range(size, len(arr)):
                res[i] = res[i - 1] - arr[i - size] + arr[i]

        makeWindow(arr, Lsum, L)
        makeWindow(arr, Msum, M)

        res = 0
        for i in range(L - 1, len(arr)):
            for j in range(0, i - L):
                res = max(res, Lsum[i] + Msum[j])
            for j in range(i + M, len(arr)):
                res = max(res, Lsum[i] + Msum[j])

        return res

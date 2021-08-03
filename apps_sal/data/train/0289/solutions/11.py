class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)

        arr = [A[0]]
        for i in range(1, n):
            arr.append(arr[-1] + A[i])
        arr = arr + [0]

        _max = 0
        for i in range(n - L + 1):
            for j in range(n - M + 1):
                if (i <= j <= i + L - 1) or (j <= i <= j + M - 1):
                    continue
                tmp = (arr[i + L - 1] - arr[i - 1]) + (arr[j + M - 1] - arr[j - 1])
                _max = max(_max, tmp)
        return _max

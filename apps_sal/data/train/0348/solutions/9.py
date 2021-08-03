class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        bestFromS = [arr[0]]
        for i in range(1, len(arr)):
            bestFromS.append(max(arr[i], arr[i] + bestFromS[i - 1]))

        bestFromE = [0] * len(arr)
        bestFromE[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            bestFromE[i] = max(bestFromE[i + 1] + arr[i], arr[i])

        res = max(bestFromS)
        for i in range(len(arr)):
            before = 0 if i == 0 else bestFromS[i - 1]
            after = 0 if (i == len(arr) - 1) else bestFromE[i + 1]
            res = max(res, before + after)

        return res

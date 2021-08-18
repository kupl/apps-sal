class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        N = len(arr1)
        a = [arr1[i] + arr2[i] + i for i in range(N)]
        b = [arr1[i] + arr2[i] - i for i in range(N)]
        c = [arr1[i] - arr2[i] + i for i in range(N)]
        d = [arr1[i] - arr2[i] - i for i in range(N)]
        return max(
            max(x) - min(x)
            for x in (a, b, c, d)
        )

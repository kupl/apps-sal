class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        a = [arr1[i] + arr2[i] - i for i in range(n)]

        mn = 10 ** 20
        ans = 0

        for i in a[::-1]:
            ans = max(ans, i - mn)
            mn = min(mn, i)

        a = [arr1[i] - arr2[i] - i for i in range(n)]

        mn = 10 ** 20

        for i in a[::-1]:
            ans = max(ans, i - mn)
            mn = min(mn, i)

        a = [arr1[i] - arr2[i] + i for i in range(n)]

        mn = 10 ** 20

        for i in a:
            ans = max(ans, i - mn)
            mn = min(mn, i)

        a = [arr1[i] + arr2[i] + i for i in range(n)]

        mn = 10 ** 20

        for i in a:
            ans = max(ans, i - mn)
            mn = min(mn, i)

        return ans

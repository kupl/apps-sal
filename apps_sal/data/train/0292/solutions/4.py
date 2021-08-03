class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        mn = 10**7
        mx = -10**7
        mn1 = 10**7
        mx1 = -10**7
        mn2 = 10**7
        mx2 = -10**7
        mn3 = 10**7
        mx3 = -10**7
        for j in range(len(arr1)):
            tmp = arr1[j] + arr2[j] + j
            tmp1 = arr1[j] - arr2[j] + j
            tmp2 = -arr1[j] + arr2[j] + j
            tmp3 = -arr1[j] - arr2[j] + j
            mn = min(mn, tmp)
            mx = max(mx, tmp)
            mn1 = min(mn1, tmp1)
            mx1 = max(mx1, tmp1)
            mn2 = min(mn2, tmp2)
            mx2 = max(mx2, tmp2)
            mn3 = min(mn3, tmp3)
            mx3 = max(mx3, tmp3)

        return max((mx - mn), mx1 - mn1, mx2 - mn2, mx3 - mn3)

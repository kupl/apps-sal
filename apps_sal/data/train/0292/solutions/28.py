class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for x in (1, -1):
            for y in (1, -1):
                minn = arr1[0] * x + arr2[0] * y
                for i in range(len(arr1)):
                    curr = arr1[i] * x + arr2[i] * y + i
                    minn = min(minn, curr)
                    ans = max(ans, curr - minn)
        return ans

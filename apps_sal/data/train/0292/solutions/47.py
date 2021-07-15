class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = -math.inf
        n = len(arr1)
        for a in (-1, 1):
            for b in (-1, 1):
                for c in (-1, 1):
                    x = -math.inf
                    y = math.inf
                    for i, v in enumerate(arr1):
                        x = max(x, a*i + b*v + c*arr2[i])
                        y = min(y, a*i + b*v + c*arr2[i])
                    ans = max(ans, x - y)
        return ans

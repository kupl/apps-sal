class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        n = len(arr1)
        for (x, y) in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            smallest = x * arr1[0] + y * arr2[0] + 0
            for i in range(n):
                cur = x * arr1[i] + y * arr2[i] + i
                ans = max(ans, cur - smallest)
                smallest = min(smallest, cur)
        return ans

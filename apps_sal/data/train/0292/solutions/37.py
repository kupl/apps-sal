class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for p, q in [(-1,-1), (1, -1), (-1, 1), (1, 1)]:
            min_v = max_v = p*arr1[0] + q*arr2[0]
            for i in range(1, len(arr1)):
                v = p*arr1[i] + q*arr2[i] + i
                min_v = min(min_v, v)
                max_v = max(max_v, v)
            ans = max(ans, max_v- min_v)
            
        return ans  

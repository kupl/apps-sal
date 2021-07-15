class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadane(arr):
            res, curr = float('-inf'), 0
            for a in arr:
                curr = max(curr+a, a)
                res = max(res, curr)
                
            return res
        
        if k==1: return kadane(arr)
        one_sum = sum(arr)
        if one_sum<0: return max(0, kadane(arr*2))
        return (one_sum*(k-2)+kadane(2*arr))%(10**9+7)


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def kadane(lst):
            max_sub = local = 0
            for n in lst:
                max_sub = max(max_sub, local := max(local + n, n))    
            return max_sub
        if k==1 or sum(arr) <= 0:
            return kadane(arr * min(2, k))
        else:
            m = 10**9+7
            return ((kadane(arr) + (k-1)*sum(arr)) % m)

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        
        def partition(arr, left, right, cache):
            if (left, right) in cache:
                return cache[(left, right)]
            if left >= right:
                return 0
            result = sys.maxsize
            for k in range(left, right):
                
                root_val = max(arr[left:k+1]) * max(arr[k+1:right+1])
                result = min(result, root_val + partition(arr, left, k, cache) + partition(arr, k+1, right, cache))
            cache[(left, right)] = result
            return result
        
        cache = {}
        partition(arr, 0, n-1, cache)
        return cache[(0, n-1)]

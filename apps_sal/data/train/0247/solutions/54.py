class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)        
        
        def get_dp(arr):
            dp = []
            ptr = 0
            total = 0
            min_val = float('inf')
            for i in range(n):
                total += arr[i]
                while ptr < i and total > target:
                    total -= arr[ptr]
                    ptr += 1
                if total == target:
                    min_val = min(min_val, i - ptr + 1)
                dp.append(min_val)
            return dp
        dp_left = get_dp(arr)
        dp_right = get_dp(arr[::-1])[::-1]
        
        min_val = float('inf')
        for i in range(n-1):
            min_val = min(min_val, dp_left[i] + dp_right[i+1])
        return min_val if min_val != float('inf') else -1

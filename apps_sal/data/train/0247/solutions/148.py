class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        left = [float('inf')]*n
        memo = {0:-1}
        current = 0
        for k in range(n):
            if k > 0:
                left[k] = left[k-1]
            current += arr[k]
            if current - target in memo:
                left[k] = min(left[k], k - memo[current - target])
            memo[current] = k
        print(left)
        
        right = [float('inf')]*n
        memo = {0:n}
        current = 0
        for k in range(n-1, -1, -1):
            if k < n-1:
                right[k] = right[k+1]
            current += arr[k]
            if current - target in memo:
                right[k] = min(right[k], memo[current-target] - k)
            memo[current] = k
        
        ans = float('inf')
        for k in range(n-1):
            ans = min(ans, left[k] + right[k+1])
        return ans if ans != float('inf') else -1


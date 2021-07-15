class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        arr1.insert(0, -1)
        arr2.sort()
        
        # dp[i][k] means the minimum number we can have at ith position with k operations
        dp = [[sys.maxsize for k in range(n + 1)] for i in range(n + 1)]
        dp[0][0] = -1
        
        for i in range(1, n + 1):
            for k in range(i + 1):
                if dp[i - 1][k] < arr1[i]:
                    # not assign
                    dp[i][k] = arr1[i]
                
                if k >= 1:
                    num = self.helper(arr2, dp[i - 1][k - 1])
                    if num > dp[i - 1][k - 1]:
                        dp[i][k] = min(dp[i][k], num)
        
        ans = sys.maxsize
        for k in range(n + 1):
            if dp[n][k] < sys.maxsize:
                ans = min(ans, k)
        return ans if ans < sys.maxsize else -1

    def helper(self, arr, val):
        # find in arr the smallest number that is larger than val
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] <= val:
                start = mid
            else:
                end = mid
        
        if arr[start] > val:
            return arr[start]
        return arr[end]

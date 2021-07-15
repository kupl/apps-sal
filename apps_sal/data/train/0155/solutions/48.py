class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        l = []
        n = len(arr)
        for i in range(n):l.append([arr[i], i])
        l.sort()
        l = [i[1] for i in l]
        
        dp = [1] * n
        for i in l:
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[i] > arr[j]:dp[i] = max(dp[i], dp[j] + 1)
                else:break
            for j in range(i - 1, max(-1, i - d -1), -1):
                if arr[i] > arr[j]:dp[i] = max(dp[i], dp[j] + 1)
                else:break
        return max(dp)

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        m = len(arr1)
        n = len(arr2)
        newarr2 = [arr2[0]]
        for i in range(1, n):
            if arr2[i] != newarr2[-1]:
                newarr2.append(arr2[i])
                
        arr2 = newarr2
        n = len(arr2)

        IL = 10 ** 9 + 7
        
        dp = [[IL for j in range(n + 1)] for i in range(m)]
        
        dp[0][n] = 0
        for i in range(n):
            if arr2[i] < arr1[0]:
                dp[0][i] = 1
            else:
                break
        
        for i in range(1, m):
            idx = 0
            if arr2[0] > arr1[i - 1]:
                dp[i][0] = dp[i - 1][n] + 1
            
            for k in range(1, n):
                a = dp[i - 1][n] + 1 if dp[i - 1][n] != IL and arr1[i - 1] < arr2[k] else IL
                b = dp[i - 1][idx] + 1 if dp[i - 1][idx] != IL else IL
                dp[i][k] = min(a, b)
                if dp[i - 1][k] < dp[i - 1][idx]:
                    idx = k
                    
            if dp[i - 1][n] != IL and arr1[i] > arr1[i -1]:
                dp[i][n] = dp[i - 1][n]
            
            for k in range(n):
                if dp[i - 1][k] != IL and arr2[k] < arr1[i]:
                    dp[i][n] = min(dp[i][n], dp[i - 1][k])
                    
        m = min(dp[m - 1])
        
        return m if m != IL else -1
        
                


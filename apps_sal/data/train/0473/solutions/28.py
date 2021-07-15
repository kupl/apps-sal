class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        
        dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
        
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                a = 0
                # [i, j - 1]
                if j == i:
                    a = arr[i]
                else:
                    a = dp[i][j - 1] ^ arr[j]
                dp[i][j] = a
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if dp[i][j] == 0:
                    res += (j - i)
        return res

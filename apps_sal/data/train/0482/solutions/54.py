class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        We can use an upper triangular matrix to represent the tree structure.
        Each diagonal element stores the value of a leaf node.        
        We calculate the largest leaf value for each possible subtree containing leaf i to j, denoted by max_leaf_value[i,j].
        We initialize max_leaf_value[i,i] = arr[i] and max_leaf_value[i,j] = 0 for i!=j.
        We store this value in the corresponding off-diagonal element.
        Let dp[i,j] denote the smallest possible sum of the values of each non-leaf node of the subtree containing leaf i to j.
        We initialize dp[i,j] = inf, i<j.
        We can apply dynamic programming in the following way:
        dp[i,j] = min(d[i,j], d[i,k] + d[k+1,j] + max_leaf_value[i,k] * max_leaf_value[k+1,j]) for k=i,...,j-1
        """
        dp = [[float('inf') for i in range(len(arr))] for j in range(len(arr))]
        for i in range(0, len(arr)):
            dp[i][i] = 0
        for l in range(2, len(arr) + 1):
            for i in range(0, len(arr) - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    ans = max(max(arr[i:k + 1]), 0) * max(max(arr[k + 1:j + 1]), 0) + dp[i][k] + dp[k + 1][j]
                    dp[i][j] = min(dp[i][j], ans)
        return dp[0][len(arr) - 1]

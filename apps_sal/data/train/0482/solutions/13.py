class Solution:

    def mctFromLeafValues(self, arr):
        """
        We can use an upper triangular matrix dp[i,j], i<=j, to represent the tree structure.
        Each diagonal element dp[i,i] stores the value of a leaf node arr[i].
        Each off-diagonal element dp[i,j], i<j, denotes the smallest possible sum of the values of each non-leaf node of the subtree containing leaf i to j.
        We initialize dp[i,j] = inf for i<j-1; dp[i,j] = arr[i] * arr[j] for i=j-1; dp[i,j] = arr[i] for i=j.
        We can apply dynamic programming in the following way:
        dp[i,j] = min(d[i,j], (d[i,k] if i<k else 0) + (d[k+1,j] if k+1<j else 0) + max[i,k] * max[k+1,j]) for k=i,...,j-1, j>i

        Improvement 1:
        We calculate the largest leaf value for each possible subtree containing leaf i to j.
        We store those values in the matrix max_leaf_value[i,j].
        We initialize max_leaf_value[i,i] = arr[i] and max_leaf_value[i,j] = 0 for i!=j.
        """
        maxi = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        for i in range(len(arr)):
            maxi[i][i] = arr[i]
        for l in range(1, len(arr) - 1):
            for i in range(len(arr) - l):
                j = i + l
                maxi[i][j] = max(maxi[i][j - 1], maxi[i + 1][j])
        dp = [[float('Inf') for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = arr[i]
        for l in range(1, len(arr)):
            for i in range(0, len(arr) - l):
                j = i + l
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], (dp[i][k] if i < k else 0) + (dp[k + 1][j] if k + 1 < j else 0) + maxi[i][k] * maxi[k + 1][j])
        return dp[0][len(arr) - 1]

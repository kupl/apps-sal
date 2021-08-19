class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        def dfs(i, partitions):
            if partitions == 1:
                return (cum[len(A)] - cum[i - 1]) / (len(A) - i + 1)
            mem[partitions][i] = 0
            for j in range(i, len(A) + 1):
                if mem[partitions - 1][j] == 0:
                    mem[partitions - 1][j] = dfs(j, partitions - 1)
                if j > i:
                    mem[partitions][i] = max(mem[partitions][i], mem[partitions - 1][j] + (cum[j - 1] - cum[i - 1]) / (j - i))
                else:
                    mem[partitions][i] = max(mem[partitions][i], mem[partitions - 1][j])
            return mem[partitions][i]
        ans = 0
        cum = [0 for i in range(len(A) + 1)]
        mem = [[0 for i in range(len(A) + 1)] for j in range(K + 1)]
        cum[0] = 0
        for i in range(len(A)):
            cum[i + 1] = cum[i] + A[i]
        return dfs(1, K)

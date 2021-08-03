class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        max_l = 0
        cache = [[0 for j in range(n)] for i in range(n)]
        a_dict = {number: index for (index, number) in enumerate(A)}

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if j == n - 1:
                    cache[i][j] = 2
                else:
                    target = A[i] + A[j]
                    if target in a_dict:
                        cache[i][j] = cache[j][a_dict[target]] + 1

                    else:
                        cache[i][j] = 2
                if cache[i][j] > 2:
                    max_l = max(cache[i][j], max_l)
        return max_l

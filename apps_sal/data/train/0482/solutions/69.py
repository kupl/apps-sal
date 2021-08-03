import math


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.memo = {}

        def dp(i, j):
            if i == j:
                self.memo[(i, j)] = [0, arr[i]]
                return self.memo[(i, j)]

            if (i, j) in self.memo:
                return self.memo[(i, j)]
            else:
                local_max = -math.inf
                local_sum = math.inf
                for k in range(i, j):
                    [left_sum, left_max] = dp(i, k)
                    [right_sum, right_max] = dp(k + 1, j)
                    local_max = max(local_max, left_max, right_max)
                    local_sum = min(local_sum, left_sum + right_sum + left_max * right_max)

                self.memo[(i, j)] = [local_sum, local_max]
                return self.memo[(i, j)]

        return dp(0, len(arr) - 1)[0]

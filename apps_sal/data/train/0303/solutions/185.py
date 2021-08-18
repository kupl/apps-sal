'''
So this can be a subproblem of different lengths of k and subarrays

so f([1,15,7,9,2,5,10]) = 1 + f([15,7,9,2,5,10]]) or 15 * 2 + f([7,9,2,5,10]]) or 
                            15 * 3 + f([7,9,2,5,10]])
                            
if not arr, then we return
'''


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)

        memo = {}

        def maxSum2(i):
            if i >= N:
                return 0
            if i in memo:
                return memo[i]
            val = -1
            sol = -1
            for j in range(1, min(k + 1, N - i + 1)):
                val = max(val, arr[i + j - 1])
                sol = max(sol, val * j + maxSum2(i + j))
            memo[i] = sol
            return sol
        return maxSum2(0)

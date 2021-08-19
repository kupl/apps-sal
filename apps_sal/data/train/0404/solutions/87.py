class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        l_A = len(A)
        memo = {(l_A, 0): 0}

        def dfs(idx, rem):
            if rem == 0 or l_A - idx < rem:
                return 0
            if rem == 1:
                return sum(A[idx:]) / (l_A - idx)
            if (idx, rem) in memo:
                return memo[idx, rem]
            sum_so_far = 0
            avg = 0
            best = 0
            for i in range(idx, l_A):
                sum_so_far += A[i]
                avg = sum_so_far / (i - idx + 1)
                best = max(best, avg + dfs(i + 1, rem - 1))
            memo[idx, rem] = best
            return best
        return dfs(0, K)

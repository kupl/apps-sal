class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        memoDict = {}

        def recurse(i, k):
            n = len(A)
            max_win = n - i - (k - 1)
            if (i, k) in memoDict:
                return memoDict[i, k]
            if k == 0:
                return sum(A[i:]) / (n - i)
            else:
                max_sum = 0
                for ind in range(1, max_win):
                    lul = recurse(i + ind, k - 1) + sum(A[i:i + ind]) / ind
                    max_sum = max(max_sum, lul)
                memoDict[i, k] = max_sum
                return max_sum
        flips = recurse(0, K - 1)
        return flips

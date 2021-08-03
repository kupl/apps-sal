class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        h = {}

        def helper(curr, pos, k):
            if pos == len(A):
                return curr
            if k == 0:
                return float('-inf')
            if (pos, k) in h:
                return curr + h[(pos, k)]
            res = 0
            for i in range(pos, len(A)):
                temp = sum(A[pos: (i + 1)]) / (i - pos + 1)
                res = max(helper(temp, i + 1, k - 1), res)
            h[(pos, k)] = res
            return curr + res

        return helper(0, 0, K)

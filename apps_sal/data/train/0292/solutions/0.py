# https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/340075/c%2B%2B-beats-100-(both-time-and-memory)-with-algorithm-and-image
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        N = len(arr1)
        a = [arr1[i] + arr2[i] + i for i in range(N)]
        b = [arr1[i] + arr2[i] - i for i in range(N)]
        c = [arr1[i] - arr2[i] + i for i in range(N)]
        d = [arr1[i] - arr2[i] - i for i in range(N)]
        return max(
            max(x) - min(x)
            for x in (a, b, c, d)
        )

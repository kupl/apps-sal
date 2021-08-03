class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        A, B, C, D = [], [], [], []
        # https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/340075/c++-beats-100-(both-time-and-memory)-with-algorithm-and-image
        # much easier to understand.
        # we need to break the four absolute value and reduce them. We can see there are 8 cases but only 4 cases. We generate 4 arrays and compute max() - min()
        for i in range(len(arr1)):
            x = arr1[i] + arr2[i] + i
            y = arr1[i] - arr2[i] - i
            z = arr1[i] + arr2[i] - i
            t = arr1[i] - arr2[i] + i
            A.append(x)
            B.append(y)
            C.append(z)
            D.append(t)

        return max(list([max(x) - min(x) for x in [A, B, C, D]]))

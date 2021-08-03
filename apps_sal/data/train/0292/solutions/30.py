class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        A, B, C, D = [], [], [], []
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

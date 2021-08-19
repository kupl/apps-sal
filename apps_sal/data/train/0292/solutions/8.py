class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        arrA = [0] * len(arr1)
        arrC = [0] * len(arr1)
        arrD = [0] * len(arr1)
        arrB = [0] * len(arr1)
        for i in range(len(arr1)):
            arrA[i] = arr1[i] + arr2[i] + i
            arrB[i] = -arr1[i] + arr2[i] + i
            arrC[i] = arr1[i] - arr2[i] + i
            arrD[i] = -arr1[i] - arr2[i] + i
        minA = arrA[0]
        minB = arrB[0]
        minC = arrC[0]
        minD = arrD[0]
        res = 0
        for i in range(1, len(arrA)):
            minA = min(minA, arrA[i])
            minB = min(minB, arrB[i])
            minC = min(minC, arrC[i])
            minD = min(minD, arrD[i])
            res = max(res, arrA[i] - minA, arrB[i] - minB, arrC[i] - minC, arrD[i] - minD)
        return res
        dic1A = {}
        dic2A = {}
        dic1A = {}
        dic2A = {}
        dic2 = {}

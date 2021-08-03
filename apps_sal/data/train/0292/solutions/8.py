class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        # j>i
        # =max(arr1[j]-arr1[i]+arr2[j]-arr2[i]+j-i,
        #     arr1[i]-arr1[j]+arr2[j]-arr2[i]+j-i,
        #     arr1[j]-arr1[i]+arr2[i]-arr2[j]+j-i,
        #     arr1[i]-arr1[j]+arr2[i]-arr2[j]+j-i)
        # arrA=arr1+arr2
        # arrB=arr2-arr1
        # arrC=arr1-arr2
        # arrD=-arr1-arr2
        # arr?[j]-arr?[i]+j-i
        # (arr?[j]+j)-(arr?[i]+i)
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

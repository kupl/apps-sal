class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        4 cases:
        
        1) arr1[i] > arr1[j] and arr2[i] < arr2[j]
            remove abs
            arr1[i] - arr1[j] + arr2[j] - arr2[i] + j - i
            (arr1[i] - arr2[i] - i) - (arr1[j] - arr2[j] - j)
            
        2) arr1[i] > arr1[j] and arr2[i] > arr2[j]
            remove abs
            arr1[i] - arr1[j] + arr2[i] - arr2[j] + j - i
            (arr1[i] + arr2[i] - i) - (arr1[j] + arr2[j] - j)
            
        3) arr1[i] < arr1[j] and arr2[i] < arr2[j]
            remove abs
            arr1[j] - arr1[i] + arr2[j] - arr2[i] + j - i
            (arr1[j] + arr2[j] + j) - (arr1[i] + arr2[i] + i)
            
        4) arr1[i] < arr1[j] and arr2[i] > arr2[j]
            remove abs
            arr1[j] - arr1[i] + arr2[i] - arr2[j] + j - i
            (arr1[j] - arr2[j] + j) - (arr1[i] - arr2[i] + i)
        '''
        max1 = max2 = max3 = max4 = float('-inf')
        min1 = min2 = min3 = min4 = float('inf')
        for i in range(0, len(arr1)):
            tmp1 = arr1[i] - arr2[i] - i
            max1 = max(max1, tmp1)
            min1 = min(min1, tmp1)
            
            tmp2 = arr1[i] + arr2[i] - i
            max2 = max(max2, tmp2)
            min2 = min(min2, tmp2)
            
            tmp3 = arr1[i] + arr2[i] + i
            max3 = max(max3, tmp3)
            min3 = min(min3, tmp3)
            
            tmp4 = arr1[i] - arr2[i] + i
            max4 = max(max4, tmp4)
            min4 = min(min4, tmp4)
        
        return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)

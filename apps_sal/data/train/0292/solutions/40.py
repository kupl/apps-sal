class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        x = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        y = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
        z = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        w = [arr1[i] - arr2[i] - i for i in range(len(arr1))]
        
        return max(map(lambda a: max(a) - min(a), (x,y,z,w)))

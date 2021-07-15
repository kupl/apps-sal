class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        x, y, z, w = [], [], [], []
        for i in range(len(arr1)):
            x.append(arr1[i] + arr2[i] + i)
            y.append(arr1[i] + arr2[i] - i)
            z.append(arr1[i] - arr2[i] + i)
            w.append(arr1[i] - arr2[i] - i)
        
        return max(map(lambda a: max(a) - min(a), (x,y,z,w)))

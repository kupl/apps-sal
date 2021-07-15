class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        ans = float('-inf')
        maxx = [float('-inf')] * 4
        minn = [float('inf')] * 4
        for i in range(n):
            maxx[0] = max(maxx[0], arr1[i] + arr2[i] + i)
            minn[0] = min(minn[0], arr1[i] + arr2[i] + i)
            ans = max(ans, maxx[0] - minn[0])
            
            maxx[1] = max(maxx[1], arr1[i] + arr2[i] - i)
            minn[1] = min(minn[1], arr1[i] + arr2[i] - i)
            ans = max(ans, maxx[1] - minn[1])
            
            maxx[2] = max(maxx[2], arr1[i] - arr2[i] + i)
            minn[2] = min(minn[2], arr1[i] - arr2[i] + i)
            ans = max(ans, maxx[2] - minn[2])
            
            maxx[3] = max(maxx[3], arr1[i] - arr2[i] - i)
            minn[3] = min(minn[3], arr1[i] - arr2[i] - i)
            ans = max(ans, maxx[3] - minn[3])

        return ans

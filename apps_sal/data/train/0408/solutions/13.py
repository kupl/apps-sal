class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        s = sum(arr)
        m = max(arr)
        if s <= target:
            return m
        l, r = 1, m+1
        while l < r:
            mid = (l+r) // 2
            cur = self.getSum(arr, mid)
            if cur == target:
                return mid
            elif cur < target:
                l = mid+1
            else:
                r = mid
        s1 = self.getSum(arr, l)
        s2 = self.getSum(arr, l-1)
        return l if abs(s1-target) < abs(s2-target) else l-1
    
    def getSum(self, arr, mid):
        s = 0
        for i in range(len(arr)):
            s += mid if arr[i] > mid else arr[i]
        return s


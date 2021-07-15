class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        preSum = [0]
        for num in arr:
            preSum.append(preSum[-1]+num)
        arrLen = len(arr)
        
        def checkSum(x):
            l = 0
            r = arrLen - 1
            if x <= arr[0]:
                return x*arrLen
            if x >= arr[r]:
                return preSum[r+1]
            while r > l:
                m = (r + l)//2
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m
            return preSum[l] + (arrLen-l)*x
        
        ll = 0
        rr = arr[-1]
        if preSum[arrLen] <= target:
            return arr[arrLen - 1]
        while rr > ll:
            mm = (rr + ll) // 2
            if checkSum(mm) < target:
                ll = mm + 1
            else:
                rr = mm
        if abs(checkSum(ll) - target) >= abs(checkSum(ll-1) - target):
            return ll - 1
        else:
            return ll
        


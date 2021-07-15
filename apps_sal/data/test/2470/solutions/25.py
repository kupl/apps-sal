class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        def bs(arr, l, r, target):
            while l<=r:
                m = l+(r-l)//2
                if arr[m]>target:
                    r = m-1
                else:
                    l = m+1
            return l
        
        arr2.sort()
        N = len(arr2)
        dp = {-1:0}
        
        for a in arr1:
            dp2 = {}
            for prev in dp:
                if a>prev:
                    dp2[a] = min(dp2.get(a, float('inf')), dp[prev])
                
                idx = bs(arr2, 0, N-1, prev)
                if idx<N:
                    dp2[arr2[idx]] = min(dp2.get(arr2[idx], float('inf')), dp[prev]+1)
                    
            dp = dp2
            if not dp:
                return -1
            
        return min(dp.values())

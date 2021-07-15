class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        if not arr1: return 0
        if not arr2: return arr1 == sorted(arr1)
        
        arr2 = sorted(list(set(arr2)), reverse=True)
        
        n, m, inf = len(arr1), len(arr2), float('inf')
        f = [[inf]*(n+1) for _ in range(n)]
        for i in range(n+1):
            f[0][i] = min(arr1[0],arr2[-1])
        f[0][0] = arr1[0]
        for i in range(1,n):
            found_k = 0
            for j in range(n+1):
                if f[i-1][j] < arr1[i]: f[i][j] = arr1[i]
                if not j: continue
                va = f[i-1][j-1]
                if not found_k:
                    if arr2[0] > va:
                        l,r = 0,m-1
                        while l < r:
                            mid = l+r+1 >> 1
                            if arr2[mid] > va:
                                l = mid
                            else: 
                                r = mid - 1
                        k = l
                        found_k = 1
                        f[i][j] = min(f[i][j],arr2[k])
                else:
                    while k+1 < m and arr2[k+1] > va: k += 1
                    f[i][j] = min(f[i][j],arr2[k])
        for i,v in enumerate(f[-1]): 
            if v < inf: return i
        return -1
                
                
                


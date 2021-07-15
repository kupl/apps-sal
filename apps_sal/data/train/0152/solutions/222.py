class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        def isFeasible(mid, arr, n, k): 
            pos = arr[0] 
            elements = 1
            for i in range(1, n): 
                if (arr[i] - pos >= mid):
                    pos = arr[i] 
                    elements += 1
                    if (elements == k): 
                        return True
            return False

        p.sort()
        #[1,2,3,4,5,100000]
        #Cm(n)
        n = len(p) 
        res = -1
        left = 0
        right = p[n - 1]
  
        while left < right: 
            mid = (left + right) // 2
            if (isFeasible(mid, p, n, m)): 
                res = max(res, mid) 
                left = mid + 1
            else: 
                right = mid 
  
        return res
            
            


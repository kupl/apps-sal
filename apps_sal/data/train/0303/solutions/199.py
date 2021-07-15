class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr == [] or k == 0:
            return 0 
        
        if len(arr) == 1 and k == 1:
            return arr[0] 
        
        l = len(arr)
        res = [0]*(l)

        for i in range(0, l):
            sub_max = 0
            for j in range(k):
                if j <= i:
                    sub_max = max(sub_max, arr[i-j])
                    res[i] = max(res[i], sub_max*(j + 1) + (res[i-j-1] if i-j-1 >=0 else 0))
        
        return res[l-1]

     

        
        

            


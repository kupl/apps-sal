class Solution:
    def longestMountain(self, A: List[int]) -> int:
        import copy 
        
        if not A:
            return 0
        
        dp = []
        B = copy.deepcopy(A)
        B.insert(0, A[0])
        B.append(A[-1])
        
        for i in range(1,len(B) - 1):
            
            if (B[i-1] < B[i] and B[i+1] < B[i]):
                dp.append(i-1)
                
            
        ret = []
        A.append(A[-1])
        for top in dp:
            
            
            left = top
            while A[left - 1] < A[left] and left > 0:
                left -= 1
            
            right = top
            while A[right + 1] < A[right]:
                right +=1
                
            print(right, left)
            ret.append(right -left + 1)
            
        print(dp, ret)
        
                
        return max(ret) if ret else 0

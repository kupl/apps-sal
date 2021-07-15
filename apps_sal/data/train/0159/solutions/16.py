class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq=collections.deque()
        
        m=-sys.maxsize
        for i,n in enumerate(nums):
            fi = n
            
            if dq:
                fi += max(dq[0][1], 0)
            while dq and fi>=dq[-1][1]:
                dq.pop()
                
            dq.append([i,fi])
            
            if i-dq[0][0]==k:
                dq.popleft()
                
            if fi>m:
                m=fi
                
        return m
            
            
        
        


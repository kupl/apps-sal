class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        
#         left, right = 0, 0 
#         _sum = 0
#         out = sys.maxsize
#         while right<len(A): 
#             _sum += A[right]
            
#             while left<=right and _sum>=k:
#                 if right-left+1<out: 
#                     out = right-left+1
#                 _sum -= A[left]
#                 left +=1
            
                
#             right +=1
            
#         return out if out!=sys.maxsize else -1

# Fail example
#     [84,-37,32,40,95]
# 167
        prefixSum = [0] 
    
        for i in range(len(A)): 
            prefixSum.append(prefixSum[-1]+A[i])

        q = collections.deque()
        out = sys.maxsize
        
        for i in range(len(prefixSum)): 
            
            while q and prefixSum[i] - prefixSum[q[0]]>=k: 
                out = min(out, i-q.popleft())
            
            while q and prefixSum[i] <= prefixSum[q[-1]]: 
                q.pop()
                
            q.append(i)
            
                
            # q.append(i)
            
        return out if out!=sys.maxsize else -1

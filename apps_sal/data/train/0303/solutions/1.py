class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
#         i = 0
#         temp = deque()
#         orig_k = K
#         while i < len(A):
#             temp.append(max(A[i:K]))
#             i = K
#             K *= 2
#         print(temp)
        
#         answer = deque()
#         while temp:
#             for _ in range(len(temp)):
#                 current_max = max(temp)
#                 #print(current_max)
#                 for _ in range(orig_k):
#                     answer.append(current_max)
#                     if len(answer) == len(A):
#                         break
#                     print(answer)
#                 temp.remove(current_max)
#         return sum(answer)

        ans=[0]
        
        for r, n in enumerate(A):
            maxVal, curVal = 0, 0
            
            for l in range(max(0, r-K+1), r+1)[::-1]:
                if A[l]>maxVal:
                    maxVal=A[l]
                
                if ans[l]+(r-l+1)*maxVal>curVal:
                    curVal=ans[l]+(r-l+1)*maxVal
           
            ans.append(curVal)
        
        return ans[-1]
                    


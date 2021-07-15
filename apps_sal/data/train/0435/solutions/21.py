class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = [0]
        for idx, i in enumerate(A):
            prefix_sum.append(i+prefix_sum[idx])
        print(prefix_sum)
        
        # now we go through and try to see if we've seen the pair number already
        
        num_enc = dict()
        total = 0
        for i in prefix_sum:
            if (i%K) in num_enc:
                total+=num_enc[i%K]
            if (i%K - K) in num_enc:
                total+=num_enc[i%K - K]
            if i%K not in num_enc:
                num_enc[i%K] = 0
            num_enc[i%K]+=1
        return total
            
            
                

        
#         total = 0
#         for i in range(0, len(A)):
#             curr_sum = A[i]
#             if curr_sum%K==0:
#                 total+=1
#             for j in range(i+1, len(A)):
#                 curr_sum+=A[j]
#                 if curr_sum%K==0:
#                     total+=1
#         return total
                
                
                
                
                
#         for wsize in range(1, len(A)):
#             i = 0
#             curr_sum = sum(A[j] for j in range(0, wsize+1))
#             while i + wsize < len(A):
                
#                 if i != 0:
#                     curr_sum-=A[i-1]
#                     curr_sum+=A[i+wsize]
#                 if curr_sum%5==0:
#                     total+=1
#                 print(i, i+wsize, wsize, curr_sum)
#                 i+=1
#         return total


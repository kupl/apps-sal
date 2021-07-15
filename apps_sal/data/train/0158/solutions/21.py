class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        self.min = float('inf')
        A = list(A)
        B = list(B)
        
        def swap(a,b):
            A[a], A[b] = A[b], A[a]
        
        @lru_cache(None)
        def helper(left, right, AB):                        
            ok = True
            swaps = 0
            
            while A != B:
                ok = False
                a = A[left]
                b = B[right]

                if a != b:
                    minn = float('inf')
                    poss = []
                    for i,c in enumerate(A):
                        if b == c and i >= left:
                            poss.append(i)
                
                    # if len(poss) > 1:
                    for p in poss:
                        swap(left,p)
                        otherswaps = helper(left+1,right+1, tuple(A+B))
                        swap(left,p)
                        minn = min(otherswaps, minn)
                        
                    return swaps+ 1 + minn
                    # else:
                    #     if poss:
                    #         # print(A,B, a,b)
                    #         swap(left,poss[0])
                    #         swaps += 1 

                left = (left+1) % len(A)
                right= (right+1) % len(B)
            
            return swaps

#         left = right = 0
#         ok = True
#         swaps = 0
#         while A != B:
#             ok = False
#             a = A[left]
#             b = B[right]
            
#             if a != b:
#                 # indx = A.index(b)
#                 for i,c in enumerate(A):
#                     if b == c and i >= left:
#                         indx = i
#                         break
#                 swap(left,indx)
#                 swaps += 1
            
#             left = (left+1) % len(A)
#             right= (right+1) % len(B)
        
        f = helper(0,0, tuple(A+B))
        print(A)
        print(B)
            
        # out = helper(A, 0, 0)
        # print(out)
        return f
                


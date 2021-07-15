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
                
                left = (left+1) % len(A)
                right= (right+1) % len(B)
            
            return swaps

        
        f = helper(0,0, tuple(A+B))
        return f
                


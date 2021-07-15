class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        B_index = collections.defaultdict(list)
        for i in range(len(B)):
            B_index[B[i]].append(i)
    
        memory = {}
    
        def helper(A_i_, B_i):
            
            A_i = A_i_
            if (A_i, B_i) in memory:
                return memory[(A_i, B_i)]
            
            while A_i < len(A):
                
                # check A match with B:
                if A[A_i] in B_index:
                    for b_i in B_index[A[A_i]]:
                        if b_i < B_i:
                            continue
                        res = max(1 + helper(A_i+1, b_i+1), helper(A_i+1, B_i))
                        memory[(A_i_, B_i)] = res   
                        return res
    
                A_i += 1
            
            memory[(A_i_, B_i)] = 0
            return 0
        
        return helper(0, 0)


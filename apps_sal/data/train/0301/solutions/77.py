class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [-1] + A
        B = [-1] + B
        
        #142
        #121
        
        #0000
        #0111
        #0111
        #0122
        
        w = len(A)
        h = len(B)
        
        dp_table = [[0 for _ in range(w)]  for _ in range(h) ]
        
        for x in range(1,w):
            for y in range(1,h):
                if A[x] == B[y]:
                    dp_table[y][x] = dp_table[y-1][x-1] +1 
                else:
                    dp_table[y][x] = max(dp_table[y][x-1],dp_table[y-1][x])
        print(dp_table)          
        return dp_table[-1][-1]


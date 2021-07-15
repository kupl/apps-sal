class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        self.N = len(A)
        self.dict1 = collections.defaultdict()
        return self.dfs(list(A), list(B), 0)
                
    
    def dfs(self,A, B, pos):
        sB = ''.join(B)
        if sB in self.dict1:
            return self.dict1[sB]
            
        if A == B:
            return 0
            
        while A[pos] == B[pos]:
            pos += 1
                
        minCnt = float('inf')
        for i in range(pos + 1, self.N):
            if B[i] == A[pos] and B[i] != A[i]:
                B[i], B[pos] = B[pos], B[i]
                tmp = self.dfs(A, B, pos + 1) + 1
                minCnt = min(tmp, minCnt)
                B[i], B[pos] = B[pos], B[i]
                    
        self.dict1[sB] = minCnt
        return minCnt


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def get_neis(s):
            res = []
            for i in range(N):
                if s[i]!=B[i]:
                    break
            
            temp = list(s)
            for j in range(i+1, N):
                if s[j]==B[i]: #and s[j]!=B[j]:
                    temp[i], temp[j] = temp[j], temp[i]
                    res.append(''.join(temp))
                    temp[i], temp[j] = temp[j], temp[i]
                    
            return res
        
        if A==B: return 0
        N = len(A)
        dq = deque([A])
        seen = set([A])
        cnt = 0
        while dq:
            length = len(dq)
            
            for _ in range(length):
                s = dq.popleft()
                
                for nei in get_neis(s):
                    if nei==B: return cnt+1
                    
                    if nei not in seen:
                        seen.add(nei)
                        dq.append(nei)
            
            cnt += 1

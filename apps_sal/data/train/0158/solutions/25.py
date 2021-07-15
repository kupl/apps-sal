class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        N = len(A)
        if not N:
            return 0
        cnt = 0
        
        q = deque()
        q.append((cnt, A, 0))
        while q:
            cnt, v, i = q.popleft()
            
            if v == B:
                return cnt
            
            for j in range(i+1, N):
                while v[i]==B[i]:
                    i += 1
                    
                if v[j]==B[i] and v[j]!=B[j]:
                    candidate = v[:i]+v[j]+v[i+1:j]+v[i]+v[j+1:]
                    q.append((cnt+1, candidate, i+1))


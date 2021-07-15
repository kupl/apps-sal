class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A, B = list(A), list(B)
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
                    candidate = v[:]
                    candidate[i], candidate[j] = candidate[j], candidate[i]
                    q.append((cnt+1, candidate, i+1))


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        visited, n = set(), len(A)
        q = collections.deque([(A, 0)])
        while q:
            C, swaps = q.popleft()
            if C == B:
                return swaps
            visited.add(C)
            i = 0
            while C[i] == B[i]: 
                i += 1
            for j in range(i + 1, n):
                if C[j] == B[i]:
                    nxt = C[:i] + C[j] + C[i+1:j] + C[i] + C[j+1:]
                    if nxt not in visited:
                        q.append((nxt, swaps + 1))
        return -1
            
            


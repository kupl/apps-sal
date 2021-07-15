class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        q = collections.deque()
        visited = set()
        q.append(A)
        visited.add(A)
        level = 0
        
        def getNext(S, B):
            S = list(S)
            res = []
            i = 0
            while i < len(S):
                if S[i] != B[i]:
                    break
                i += 1
            
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    S[j], S[i] = S[i], S[j]
                    res.append(''.join(S))
                    S[j], S[i] = S[i], S[j]
                    
            return res
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == B:
                    return level
                for next_str in getNext(curr, B):
                    if next_str not in visited:
                        q.append(next_str)
                        visited.add(next_str)
            level += 1
        
        return -1

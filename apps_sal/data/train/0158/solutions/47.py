class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        #assert(len(A) == len(B))
        #assert(sorted(A) == sorted(B))
        
        if A == B:
            return 0
        
        seen = set(A)
        q = deque()
        q.append((A,0))
        while q:
            currentString, k = q.popleft()
            
            for i in range(0, len(B)-1):
                if currentString[i] == B[i]:
                        continue
                        
                for j in range(i+1,len(B)):   
                    if currentString[j] == B[j]:
                        continue
                        
                    if currentString[i] == currentString[j]:
                        continue
                        
                    if currentString[j] != B[i]:
                        continue
                        
                    
                    newString = currentString[:i] + currentString[j] + currentString[i+1:j] + currentString[i] + currentString[j+1:]
                    
                    if newString == B:
                        return k+1
                    
                    if newString not in seen:
                        q.append((newString,k+1))
                        seen.add(newString)
                break
                    
        return -1

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(B)
        q = deque([B])
        visited = {B}
        
        cnt = 0
        
        while q:
            L = len(q)
            for _ in range(L):
                cur = q.popleft()
                if cur == A:
                    return cnt
                
                pos = 0
                while A[pos] == cur[pos]:
                    pos += 1
                    
                curlist = list(cur)
                
                for i in range(pos+1, n):
                    
                    if curlist[i] == A[pos] and curlist[i] != A[i]:
                        curlist[i], curlist[pos] = curlist[pos], curlist[i]
                        
                        curstr = ''.join(curlist)
                        if curstr not in visited:
                            q.append(curstr)
                            
                        visited.add(curstr)
                        curlist[i], curlist[pos] = curlist[pos], curlist[i]
            cnt += 1
            
        return cnt

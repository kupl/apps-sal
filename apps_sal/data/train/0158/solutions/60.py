class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def swap(s):
            i=0
            while s[i]==B[i]:
                i+=1
       
            for j in range(i+1,len(s)):
                if s[j]==B[i] and B[j]!=s[j]:
                    yield s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                    
        q=collections.deque([(A,0)])
        seen={A}
        
        while q:
            s,d=q.popleft()
            if s==B:
                return d
            for n in swap(s):
                if n not in seen:
                    seen.add(n)
                    q.append((n,d+1))
                    


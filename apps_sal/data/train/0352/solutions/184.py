class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def check(w1, w2):
            idx = 0
            
            for i in range(len(w2)):
                if w2[i]==w1[idx]:
                    idx += 1
                
                if idx==len(w1):
                    return True
            
            return False
        
        n = len(words)
        words.sort(key=lambda w: len(w))
        G = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                if len(words[j])-len(words[i])>1:
                    break
                
                if len(words[j])-len(words[i])==1 and check(words[i], words[j]):
                    G[i].append(j)
                
        def rec(v):
            if memo[v]!=-1:
                return memo[v]
            
            res = 1
            
            for nv in G[v]:
                res = max(res, rec(nv)+1)
            
            memo[v] = res
            return res
    
        memo = [-1]*n
        ans = 0
        
        for i in range(n):
            ans = max(ans, rec(i))
        
        return ans

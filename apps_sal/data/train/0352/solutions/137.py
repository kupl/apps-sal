class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.res = 0
        
        def compare(w1, w2):
            if len(w1) > len(w2):
                w1, w2 = w2, w1
                
            if len(w2) - len(w1) != 1:
                return False
            
            i, j = 0, 0
            
            flag = False
            while i < len(w1) or j < len(w2):
                if i < len(w1) and w1[i] == w2[j]:
                    i += 1
                    j += 1
                
                elif not flag:
                    flag = True
                    j += 1
                    
                else:
                    return False
                
            return True
        
        @lru_cache(maxsize=None)
        def dfs(w):
            length = 0
            for word in words:
                if len(word) - len(w) == 1 and compare(w, word):
                    length = max(dfs(word), length)
                    
            ret = length + 1
            self.res = max(ret, self.res)
            return ret
        
        for w in words:
            dfs(w)
            
        return self.res
        
                
            
        


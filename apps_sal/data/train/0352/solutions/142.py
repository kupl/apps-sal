class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        '''
        
        abc dabc
        
        max_val = max(i->(0,len(a)) f(n,i-1))
        
        '''
        def is_predessor(word1, word2):
            
            if(abs(len(word1) - len(word2)) > 1):
                return False
            else:
                count = 0
                word1_cnt = 0
                word2_cnt = 0
                
                while(word1 and word2):
                    if(word1[0] == word2[0]):
                        word1 = word1[1:]
                        word2 = word2[1:]
                    else:
                        count+=1
                        word1 = word1[1:]
                    
                    if(count > 1):
                        return False
                
                
                return True
        
            
        words = sorted(words, key = lambda x:len(x))
        
        M = [0]*len(words)
        M[0] = 1
        overall_max = float('-inf')
        for i in range(1, len(M)):
            max_val = float('-inf')
            for j in range(i):
                if((len(words[i]) != len(words[j])) and is_predessor(words[i], words[j])):
                    max_val = max(max_val, 1 + M[j])
                
            M[i] = max(1, max_val)
            overall_max = max(overall_max, M[i])
        
        return overall_max
                
            


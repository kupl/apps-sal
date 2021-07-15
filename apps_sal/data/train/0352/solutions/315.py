class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        visited = set()
        word_dict = {}
        
        for word in words:
            word_dict[word] = 1
        
        def visit(word):
            visited.add(word)
            
            for i in range(len(word)):
                child = word[:i] + word[i+1:]
                if child not in word_dict:
                    continue
                
                if child not in visited:
                    visit(child)
                
                word_dict[word] = max(word_dict[word], 1 + word_dict[child])    
        
        for word in words:
            visit(word)
        
        return max(word_dict.values())

                    
        
            


import copy
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word), reverse=True)
        wordSet = set(copy.deepcopy(words))
        visited = set()
        
        def find_chain(word, length):
            if word not in wordSet or word in visited:
                return length
            
            visited.add(word)
            max_len = 0
            for i in range(len(word)):
                tmp = copy.deepcopy(word)
                tmp = tmp[:i] + tmp[i+1:]
                
                max_len = max(find_chain(tmp, length+1), max_len)
                
            return max_len
        
        max_len = 0
        for word in words:
            max_len = max(max_len, find_chain(word, 0))
        
        return max_len
        
            
                


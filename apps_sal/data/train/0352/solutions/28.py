class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_len = [[] for _ in range(16)]
        graph = {word: [] for word in words}
        
        for word in words:
            words_len[len(word) - 1].append(word)
    
        def predecessor(word1, word2):
            for i in range(len(word2)):
                if word2[:i] + word2[i+1:] == word1:
                    return True
            
            return False
        
        for i in range(len(words_len) - 1):
            words_1 = words_len[i]
            words_2 = words_len[i + 1]
            
            for word1 in words_1:
                for word2 in words_2:
                    if predecessor(word1, word2):
                        graph[word1].append(word2)
        

        memo = {word: -1 for word in words}
        
        def dfs(word):
            t = 1
            
            if memo[word] == -1:
                for w in graph[word]:
                    t = max(t, 1 + dfs(w))
            
                memo[word] = t
                
            return memo[word]
        
        
        lpl = 0
        
        for words in words_len:
            for word in words:
                lpl = max(lpl, dfs(word))
        
        return lpl
        
        


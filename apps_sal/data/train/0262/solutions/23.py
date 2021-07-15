class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        allwords = words + [result]
        n = max(list(map(len, allwords)))
        firstc = set(word[0] for word in allwords)
        if len(result) < n : return False
        def dfs(charidx, wordidx, carry, visited, char2digit):
            if charidx == n: return carry == 0
            if wordidx == len(allwords):
                tot = sum(char2digit[word[~charidx]] if charidx < len(word) else 0 for word in words) + carry
                if (tot % 10) == char2digit[result[~charidx]]:
                    return dfs(charidx + 1, 0, tot // 10, visited, char2digit)
                return False
            if  wordidx < len(words) and charidx >= len(words[wordidx]):
                return dfs(charidx, wordidx+1, carry, visited, char2digit)
            
            c = allwords[wordidx][~charidx]
            first = 1 if c in firstc else 0
            if c in char2digit:
                return dfs(charidx, wordidx+1, carry, visited, char2digit)
            for d in range(first, 10):
                if d not in visited:
                    visited.add(d)
                    char2digit[c] = d
                    if dfs(charidx, wordidx+1, carry, visited, char2digit): return True
                    del char2digit[c]
                    visited.remove(d)
            return False
      
        return dfs(0, 0, 0, set(), {})
                    
             
                
            
            


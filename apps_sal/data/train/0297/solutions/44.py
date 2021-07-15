from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counter = Counter(tiles)
        
        def dfs(counter):
            result = len(counter)
            print(result)
            
            for character in counter:
                temp = counter.copy()
                if temp[character] == 1:
                    del temp[character]
                else:
                    temp[character] -= 1
                
                result += dfs(temp)
            
            return result
        
        result = dfs(counter)
        
        return result
            
            
        
        
        


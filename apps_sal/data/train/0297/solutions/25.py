class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(elements):
            if prev_elements:
                result.add(''.join(prev_elements))
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
            
        result = set()
        prev_elements = []
        
        dfs(list(tiles))
        
        return len(result)


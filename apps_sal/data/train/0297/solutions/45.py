class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        output = set()
        
        def helper(result, options):
            if not options:
                return
            for idx, o in enumerate(options):
                tmp = options[:]
                tmp.pop(idx)
                output.add(''.join(result + [o]))
                helper(result + [o], tmp)
            
        helper([], list(tiles))
        
        return len(output)

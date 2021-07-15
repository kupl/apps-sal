class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        moveMap = {1:[8, 6], 2:[7, 9], 3:[4, 8], 4:[3, 9, 0], 5:[], 6:[1, 7, 0],
                   7:[2, 6], 8:[1, 3], 9:[4, 2], 0:[4, 6]}
        
        memo = {}
    
        def aux(key, rem):
            if rem == 0:
                return 1
            if (key, rem) in memo: return memo[(key, rem)]
            
            count = 0
            # Move to each valid key from this key
            moves = moveMap[key]
            for m in moves:
                count += aux(m, rem - 1)
            
            # Save the result
            memo[(key, rem)] = count
            return count
        
        count = 0
        for startKey in moveMap:
            count += aux(startKey, n - 1)
            
        return count % MOD
                
            


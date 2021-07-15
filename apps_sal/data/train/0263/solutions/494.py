class Solution:
    def helper(self,cache,position,num_hops):
        neighbors = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
             [1,7,0],[2,6],[1,3],[2,4]]
        if (position, num_hops) in cache:
            return cache[ (position, num_hops) ]

        if num_hops == 0:
            return 1

        else:
            num_sequences = 0
            for neighbor in neighbors[position]:
                num_sequences += self.helper(cache,neighbor, num_hops - 1)
            cache[ (position, num_hops) ] = num_sequences
        return num_sequences
        
    def knightDialer(self, n: int) -> int:
        cache = {}
        res = 0      
        for start in range(10):
            res += self.helper(cache,start, n-1)
        return res % (10**9 + 7)
    



        
        
                    
                    
                    
                


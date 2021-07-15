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
            neighbors = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
             [1,7,0],[2,6],[1,3],[2,4]]
            prior_case = [1] * 10                                     
            current_case = [1] * 10                                   
            current_num_hops = 1                                    

            while current_num_hops < n:                       
                current_case = [0] * 10                               
                current_num_hops += 1                                 

                for position in range(0, 10):                         
                    for neighbor in neighbors[position]:              
                        current_case[position] += prior_case[neighbor]
                prior_case = current_case                             

            return sum(current_case) % (10**9 + 7)
    



        
        
                    
                    
                    
                


class Solution:
    def knightDialer(self, n: int) -> int:
        total_jumps = [1] * 10  #base case you can be placed ANYWHERE 
        #These are your neighbors where you jumping to with your knight mover 
        neighbors = { 
            0:(4,6),
            1:(6,8),
            2:(7,9),
            3:(4,8),
            4:(0,3,9),
            5:(),
            6:(0,1,7),
            7:(2,6),
            8:(1,3),
            9:(2,4)
        
        }
        
        #jumps allowed is n - 1 
        for jumps_left in range(n - 1): 
            #our next_jumps 
            next_jumps = [0] * 10 
            for num in range(0, 10): 
                for next_num in neighbors[num]: 
                    next_jumps[next_num] = next_jumps[next_num] + total_jumps[num] % (10 ** 9 + 7)
                    
            total_jumps = next_jumps
            
        return sum(total_jumps) % (10 ** 9 + 7)

                    
# class Solution():            
    # def count_sequences(start_position, num_hops):                
    #     prior_case = [1] * 10                                     
    #     current_case = [0] * 10                                   
    #     current_num_hops = 1                                      

    #     while current_num_hops <= num_hops:                       
    #         current_case = [0] * 10                               
    #         current_num_hops += 1                                 

    #         for position in range(0, 10):                         
    #             for neighbor in neighbors(position):              
    #                 current_case[position] += prior_case[neighbor]
    #         prior_case = current_case                             

    #     return current_case[start_position]              
# class Solution:
#     def knightDialer(self, n: int) -> int:
#         #knight -> up or down (2 steps) and move left or right ( 1step)
#         #knight -> move left or right (2 steps) and move up and down (1 step)
        
#         #We have a Knight as shown above
#         #We also have a numer pad and can ONLY stand on numbers 
        
#         #Given an int -> n move the knight on any numeric cell and then perform n-1 jumps to dial a number of length n 
#         #Return the answer modulo 10^9 + 7 

#         neighbors = { 
#             0:(4,6),
#             1:(6,8),
#             2:(7,9),
#             3:(4,8),
#             4:(0,3,9),
#             5:(),
#             6:(0,1,7),
#             7:(2,6),
#             8:(1,3),
#             9:(2,4)
        
#         }
    
#         cur_numpads = [1] * 10 
        
#         for pos in range(n - 1): 
#             next_numpads_num = [0] * 10
            
#             for cur_key in range(10):
#                 for next_key in neighbors[cur_key]:
#                     next_numpads_num[next_key] = next_numpads_num[next_key] + cur_numpads[cur_key] % (10 ** 9 + 7)
                    
#             cur_numpads = next_numpads_num 
        
#         return sum(cur_numpads) % (10**9 + 7)


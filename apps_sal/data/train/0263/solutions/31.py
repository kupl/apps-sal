class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        prior_case = [1] * 10
        current_case = [0] * 10
        current_num_hops = 1

        while current_num_hops < n:
            current_case = [0] * 10
            current_num_hops += 1

            for position in range(0, 10):
                for neighbor in neighbors[position]:
                    current_case[position] += prior_case[neighbor]
            prior_case = current_case

        return sum(prior_case) % (10**9 + 7)
        '''
        moves = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        prev_level = [1] * 10 
        curr_level = [0] * 10
        level = 1
        
        while level < n:
            
            for num in range(10):
                for reachable in moves[num]:
                    curr_level[reachable] += prev_level[reachable]
                    
            level += 1
            prev_level = curr_level
            curr_evel = [0] * 10
            print(sum(prev_level))
            
        return sum(prev_level)
        '''

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        size = len(position)
        
        # --------------------------------------------
        def satisfy( gap ) -> bool:
            '''
            input: gap
            output: True, if m balls can be placed with distance >= gap.
                    False, otherwise.
            '''
            
            next_valid_pos = position[0] + gap
            
            # start from smallest position
            good_positions = 1
            
            for idx in range(1, size):
                
                if position[idx] >= next_valid_pos:
                    good_positions += 1
                    next_valid_pos = position[idx] + gap
                
                if good_positions == m:
                    return True
            
            return False
        
        # --------------------------------------------
        
        # preprocessing, keep it sorted in ascending order
        position.sort()
        
        # maximum gap between two balls
        max_gap = (position[-1] - position[0]) // (m - 1)
        
        # minimum gap between two balls
        min_gap = min( position[i] - position[i-1] for i in range(1, size) )
        
        
        
        if m == 2:
            
            # Quick response for simple case
            return max_gap
        
        
        
        # launch binary search to find optimal gap
        left, right = min_gap, max_gap
        
        while left <= right:
            
            gap_trial = left + (right - left) // 2
            
            if satisfy(gap=gap_trial):
                
                # m balls can be placed with gap_trial
                # make gap_trial larger, and try again
                left = gap_trial + 1
                
            else:

                # m balls cannot be placed with gap_trial
                # make it smaller, and try again
                right = gap_trial - 1
        
        
        # because left = gap_trial + 1
        # left - 1 is the optimal gap
        return left-1
        


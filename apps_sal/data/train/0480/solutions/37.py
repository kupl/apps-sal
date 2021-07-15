class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        visited = dict()
        
        def move(cur_index, cur_step):
            if (cur_index, cur_step) in visited:
                return visited[(cur_index, cur_step)]
            if cur_index < 0 or cur_index >= arrLen:
                visited[(cur_index, cur_step)] = 0
                return 0
            
            if cur_step == steps:
                if cur_index == 0:
                    return 1
                return 0
            
            visited[(cur_index, cur_step)] = move(cur_index+1, cur_step+1) + move(cur_index-1, cur_step+1) + move(cur_index, cur_step+1)
            
            return visited[(cur_index, cur_step)]
        
        move(0, 0)
        
        return move(0, 0) % ((10**9)+7)

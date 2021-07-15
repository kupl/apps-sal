class Solution:
  
    def populate_jumps(self, sorted_values_idx, jumps):
      
      stack = []
      for jump_to in sorted_values_idx:
        
        while(stack and stack[-1] < jump_to):
          jump_from = stack.pop()
          jumps[jump_from] = jump_to
        
        stack.append(jump_to)
      
    def oddEvenJumps(self, A: List[int]) -> int:
        #always jumping forward so j >i 
        
        # odd jumps
        #right should be >= current and right should be smallest among all >= current
        
        # even jumps
        #right <= current and right should be maximum among all <= current
        
        
        
        # [10,13,12,14,15]
        
        #we can have a dp, marking if we can reach the goal node making an even or a odd numbered jump
        #brute force, for each idx i, try to make odd jump and then even jump and then see if we are able to land on last idx
        
        #we can eleiminate repeated work by remebering that if we can reach the last idx from intermediate nodes by making a odd/even jump , so we only visit each idx once
        
        #if we try to do a bottom up dp, calc if we can reach goal node from ith node each by making an odd or an even jump
        #then calc the np of indexes from where odd jump is possible
        
        
        #next task is to identify which node to jump to in case of even and odd jumps
        #we can precompute even and odd jumps for all indexes
        
        odd_jump = [None]*len(A)
        even_jump = [None]*len(A)
        
        num_idx_array = [(num, idx) for idx, num in enumerate(A)]
        
        sorted_idxs = list(map(lambda x: x[1], list(sorted(num_idx_array))))
        
        reverse_sorted_idxs = list(map(lambda x: x[1], list(sorted(num_idx_array, key= lambda x: (-x[0], x[1])))))
        
        
        self.populate_jumps(sorted_idxs, odd_jump)
        self.populate_jumps(reverse_sorted_idxs, even_jump)
        
        odd_dp = [False]*len(A)
        even_dp = [False]*len(A)
        
        odd_dp[-1] = True #goal node is always reachable from itself
        even_dp[-1] = True
        
        result = 1
        print(odd_dp, )
        #odd_dp = [F, F, F, F, T]
        #even_dp =[F, F, F, F, T]
        for start_idx in range(len(A) - 2, -1, -1):
          
          if odd_jump[start_idx] is not None and even_dp[odd_jump[start_idx]] is True:
            odd_dp[start_idx] = True
            result += 1
            
          if even_jump[start_idx] is not None and odd_dp[even_jump[start_idx]] is True:
            even_dp[start_idx] = True
            
        return result

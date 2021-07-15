class Solution:
    def build_value_index_map(self,arr):
        value_idx_map = collections.defaultdict(list)
        
        for i in range(len(arr)):
            value_idx_map[arr[i]].append(i)
        return value_idx_map
        
        
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        b_value_idx_map = self.build_value_index_map(B)
        
        
        memo = {}
        
        def helper(a_idx,b_max_idx,memo):
            if a_idx == len(A) or b_max_idx == len(B):
                return 0
            
            
            if (a_idx,b_max_idx) in memo:
                return memo[a_idx,b_max_idx]
            
            curr_num = A[a_idx]                
            res = 0

            for b_idx in b_value_idx_map.get(curr_num,[]):
                if b_idx > b_max_idx:
                    temp = 1 + helper(a_idx+1,b_idx,memo)
                    res = max(res,temp)
            
            memo[a_idx,b_max_idx] = max(res,helper(a_idx+1,b_max_idx,memo))
            return memo[a_idx,b_max_idx]
    
        res=  helper(0,-1,memo)
        return res
            


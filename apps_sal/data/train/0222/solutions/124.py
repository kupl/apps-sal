from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        num_to_idx = {n: i for i, n in enumerate(nums)}
        mat = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        path_len = 0
        for i in range(len(mat)):
            for j in range(i + 1, len(mat)):
                n = nums[j] - nums[i]
                if n < nums[i] and n in num_to_idx:
                    mat[i][j] = mat[num_to_idx[n]][i] + 1
                else:
                    mat[i][j] = 2
                    
                path_len = max(path_len, mat[i][j])
                
        return path_len if path_len >= 3 else 0
                
            
            


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        idx_table = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(n):
            for idx, person in enumerate(preferences[i]): idx_table[i][person] = idx
                
        unhappy = [0] * n
        for i in range(n//2):
            a, b = pairs[i]
            b_a_idx, a_b_idx = idx_table[b][a], idx_table[a][b]
            for j in range(i+1, n//2):
                c, d = pairs[j]
                
                c_a_idx = idx_table[c][a]
                c_b_idx = idx_table[c][b]
                c_d_idx = idx_table[c][d]
                
                d_a_idx = idx_table[d][a] 
                d_b_idx = idx_table[d][b] 
                d_c_idx = idx_table[d][c] 
                
                a_c_idx = idx_table[a][c] 
                a_d_idx = idx_table[a][d] 
                
                b_c_idx = idx_table[b][c] 
                b_d_idx = idx_table[b][d] 
                
                if c_a_idx < c_d_idx and a_c_idx < a_b_idx: unhappy[a] = unhappy[c] = 1 # a & c prefer each other
                if d_a_idx < d_c_idx and a_d_idx < a_b_idx: unhappy[a] = unhappy[d] = 1 # a & d prefer each other
                if c_b_idx < c_d_idx and b_c_idx < b_a_idx: unhappy[b] = unhappy[c] = 1 # b & c prefer each other
                if d_b_idx < d_c_idx and b_d_idx < b_a_idx: unhappy[b] = unhappy[d] = 1 # b & d prefer each other
        return sum(unhappy)

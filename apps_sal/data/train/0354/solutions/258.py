M = int(1e9 + 7)

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.roll_max = rollMax
        self.cache = {}
        return self._dfs(n, -1, 0)
    
    def _dfs(self, rolls_left: int, prev_roll: int, curr_len: int) -> None:
        if rolls_left == 0:
            return 1
        
        if (rolls_left, prev_roll, curr_len) in self.cache:
            return self.cache[(rolls_left, prev_roll, curr_len)]
        
        result = 0
        for i in range(6):
            if i == prev_roll and curr_len >= self.roll_max[i]:
                continue
                
            result += self._dfs(rolls_left - 1, i, curr_len + 1 if i == prev_roll else 1)

        result %= M 
        self.cache[(rolls_left, prev_roll, curr_len)] = result
        return result
        
        


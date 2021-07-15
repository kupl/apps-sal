class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n < 1:
            return 0
        
        def backtrack(prev_roll, count, seq_len):
            if seq_len == n:
                return 1
            
            if (prev_roll, count, seq_len) in cache:
                return cache[(prev_roll, count, seq_len)]
            result = 0

            for num in range(6):
                if num != prev_roll:
                    result += backtrack(num, 1, seq_len+1)
                elif count < rollMax[num]:
                    result += backtrack(num, count+1, seq_len+1)
            
            cache[(prev_roll, count, seq_len)] = result % MOD
            return cache[(prev_roll, count, seq_len)]
        
        MOD = (10 ** 9) + 7
        cache = {}
        return backtrack(-1, 0, 0)

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        next_moves = defaultdict(list)
        next_moves[1] = [6, 8]
        next_moves[2] = [7, 9]
        next_moves[3] = [4, 8]
        next_moves[4] = [0, 3, 9]
        next_moves[5] = []
        next_moves[6] = [0, 1, 7]
        next_moves[7] = [2, 6]
        next_moves[8] = [1, 3]
        next_moves[9] = [2, 4]
        next_moves[0] = [4, 6]
        
        solutions = [1 for _ in range(10)]
        while n > 1:
            next_solutions = []
            for last_num in range(0, 10):
                count = sum(solutions[prev] for prev in next_moves[last_num])
                if count >= MOD: count %= MOD
                next_solutions.append(count)
            solutions = next_solutions
            n -= 1
                
        return sum(solutions) % MOD
        
        
        memo = dict()
        
        def count(size, at):
            if size == 0: return 1
            if (size, at) in memo: return memo[(size, at)]
            
            c = sum(count(size - 1, next_at) for next_at in next_moves[at])
            if c >= MOD: c %= MOD
            
            memo[(size, at)] = c
            return c
        
        total_possible = sum(count(n - 1, at) for at in range(0, 10))
        return total_possible % MOD

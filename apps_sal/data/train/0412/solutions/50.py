class Solution:
    # Recursive memoized solution
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        return self.num_rolls_util(memo, d, f, target, 0, 0)
    
    
    def num_rolls_util(self, memo, d, f, target, level, cur_sum):
        if level == d:
            return cur_sum == target
        
        if (level, cur_sum) in memo:
            return memo[(level, cur_sum)]
        
        res = 0
        for i in range(1, f + 1):
            if cur_sum + i <= target:
                res += self.num_rolls_util(memo, d, f, target, level + 1, cur_sum + i)
            
        memo[(level, cur_sum)] = res
        
        return res % (10 ** 9 + 7)

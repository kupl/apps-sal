class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        return self.helper(n, rollMax, 0, 0, {}) % MOD
        
    def helper(self, n, rollMax, last, times, cache):
        if (n, last, times) in cache:
            return cache[(n, last, times)]
        
        if n == 0:
            return 1
        
        res = 0
        for i in range(6):
            if last != i + 1:
                res += self.helper(n - 1, rollMax, i + 1, 1, cache)
            elif rollMax[i] > times:
                res += self.helper(n - 1, rollMax, last, times + 1, cache)
                
        cache[(n, last, times)] = res
        return res

class Solution:
    def helper(self, keys, n, digit, cache):
        if not n:
            return 1
        
        if (n, digit) in cache:
            return cache[(n,digit)]
        
        count = 0
        for d in keys[digit]:
            count += self.helper(keys, n-1, d, cache)
        
        cache[(n,digit)] = count
        return cache[(n,digit)]
        
    def knightDialer(self, n: int) -> int:
        
        keys = {1:[6,8], 2:[7,9], 3:[4,8],4:[0,3,9], 5: [], 6:[7,1,0], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
        
        count = 0
        cache = {}
        for i in range(0, 10):
            count += self.helper(keys, n-1, i, cache)
        return count % (10**9+7)
        # def helper()


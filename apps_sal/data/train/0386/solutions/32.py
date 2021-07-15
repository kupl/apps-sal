MOD = int(1e9 + 7)

class Solution:
    def get(self, n, l):
        if n == 1:
            return 1
        
        try:
            return self.cache[(n, l)]
        except KeyError:
            ret = 0
            for next_l in self.next_letters[l]:
                ret += self.get(n - 1, next_l)
                ret %= MOD
                
            self.cache[(n, l)] = ret
            return ret
        
    def countVowelPermutation(self, n: int) -> int:
        self.next_letters = [
            [1],
            [0, 2],
            [0, 1, 3, 4],
            [2, 4],
            [0],
        ]
        self.cache = {}
        
        for nn in range(2, n + 1):
            for l in range(5):
                self.get(nn, l)
        
        ret = 0
        for l in range(5):
            ret += self.get(n, l)
            ret %= MOD
        return ret
        


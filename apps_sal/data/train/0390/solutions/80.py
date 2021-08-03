class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return self.dfs(n)

    @lru_cache(None)
    def dfs(self, remain):
        sqrt_root = int(math.sqrt(remain))
        for i in range(1, sqrt_root + 1):
            if not self.dfs(remain - i * i):
                return True

        return False

    '''
        return self.helper(n, True)
    
    def helper(self, n, label):
        value = math.sqrt(n)
        if value == int(value):
            return label
        re = False
        
        for i in range(n,0, -1):
            ii = math.sqrt(i)
            if ii == int(ii):
                print(ii, label)
                re = self.helper(n-int(ii*ii), not label)
        return re 
    '''

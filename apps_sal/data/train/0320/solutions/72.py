class Solution:
    def minOpsSingle(self, x):
        n_inc = 0
        n_db = 0
        assert(x >= 0)
        while x > 0:
            if x % 2 == 0:
                x = x // 2
                n_db += 1
            else:
                x -= 1
                n_inc += 1
        return (n_inc, n_db)
    
    def minOperations(self, nums: List[int]) -> int:
        tot_inc = 0
        tot_db = 0
        for n in nums:
            x,y = self.minOpsSingle(n)
            tot_inc += x
            tot_db = max(tot_db, y)
        return tot_inc + tot_db

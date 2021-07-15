class Solution:
    def minOperations(self, nums: List[int]) -> int:

        m = 0
        f = 0 
        for x in nums:
            
            if x == 0:
                continue
            
            c = 0
            mm = 0
            baz = x
            while x > 1:
                if x % 2 == 0:
                    x = x // 2
                    mm += 1
                else:
                    x -= 1
                    c += 1
            print((baz,c))
            f += 1 + c
            m = max(m,mm)
            print(m)
            
        f += m
        return f


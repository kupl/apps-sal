class Solution:
    def helper(self, n):
        if n == 1:
            return 0
        
        d = int(math.sqrt(n))
        cnt = 2
        sm = 1 + n
        while d > 1:
            if n % d == 0:
                d1 = n // d
                if d1 != d:
                    sm += d + d1
                    cnt += 2
                else:
                    sm += d
                    cnt += 1
            if cnt > 4:
                return 0
            
            d -= 1
        
        if cnt == 4:
            return sm
        return 0
        
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res += self.helper(n)
            #print(n, res)
        return res

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def findiv(num):
            res = 0
            cnt = 0
            for i in range(1, int(num ** 0.5) + 1):
                if not num % i:
                    if i * i == num:
                        cnt += 1
                        res += i
                    else:
                        cnt += 2
                        res += i
                        res += num // i
            return res if cnt == 4 else 0
        
        
        res = 0
        
        for num in nums:
            res += findiv(num)
        return res

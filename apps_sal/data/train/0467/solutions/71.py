class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(contr(n) for n in nums)        
    
def contr(n):
    p = None
    if n**.5%1==0:
        return 0
    for i in range(2,math.ceil(n**.5)):
        if n%i==0:
            if p is None:
                p = i
            else:
                return 0
    if p is None:
        return 0
    return 1 + p + n//p + n

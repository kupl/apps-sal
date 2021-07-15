class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def findfactors(n):
            f = []
            for i in range(1,int(n**0.5)+1):
                if n%i==0:
                    f.append(i)
                    if (i!=n//i):
                        f.append(n//i)
            return sum(f) if len(f)==4 else 0
        return sum([findfactors(x) for x in nums])


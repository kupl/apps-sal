# N = len(nums)
# time: O(NlogN)
# space: O(N)
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def make_divisors(n):
            divisors = []
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n//i)
            return len(divisors), divisors
        
        ret = [0]
        for n in nums:
            l, d = make_divisors(n)
            if l == 4:
                ret.append(sum(d))
        return sum(ret)


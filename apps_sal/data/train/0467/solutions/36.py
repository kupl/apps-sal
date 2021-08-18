class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            tmp = set([1, n])
            for d in range(2, ceil(sqrt(n)) + 1):
                if n % d == 0:
                    tmp.add(d)
                    tmp.add(n // d)
            if len(tmp) == 4:
                ans += sum(tmp)
        return ans

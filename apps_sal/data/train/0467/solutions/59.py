class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            tmp = set([1, n])
            r = ceil(sqrt(n))
            if r * r == n:
                continue
            for d in range(2, r + 1):
                if n % d == 0:
                    tmp.add(d)
                    tmp.add(n // d)
            # print(tmp)
            if len(tmp) == 4:
                ans += sum(tmp)
        return ans

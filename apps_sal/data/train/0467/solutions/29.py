class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def div_num(x):
            (ans, ssum) = (2, x + 1)
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    ans += 1 + (i * i != x)
                    ssum += i + x // i if i * i != x else i
            return (ans == 4, ssum)
        res = 0
        for x in nums:
            (flag, ssum) = div_num(x)
            if flag == 1:
                res += ssum
        return res

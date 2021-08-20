class Solution:

    def getDivisors(self, x):
        if x == 1:
            return [1]
        out = []
        bound = int(sqrt(x)) + 1
        for i in range(1, bound):
            if x % i == 0:
                out.append(i)
                if x // i != i:
                    out.append(x // i)
            if len(out) > 4:
                break
        return out

    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors = {}
        sum_four = 0
        for x in nums:
            if x in divisors:
                if len(divisors[x]) == 4:
                    sum_four += sum(divisors[x])
            else:
                x_div = self.getDivisors(x)
                if len(x_div) == 4:
                    sum_four += sum(x_div)
                divisors[x] = x_div
        return sum_four

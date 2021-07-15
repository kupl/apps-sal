class Solution:
    def sumFourDivisors(self, nums: List[int], c={}) -> int:
        r = 0
        for n in nums:
            if n in c:
                r += c[n]
                continue
            d = []
            for i in range(1, int(sqrt(n) + 1)):
                if n % i == 0:
                    d.append(i)
                    j = n // i
                    if j != i:
                        d.append(j)
                if len(d) > 4:
                    break
            if len(d) == 4:
                s = sum(d)
                c.update({n:s})
                r += s
            else:
                c.update({n:0})
        return r

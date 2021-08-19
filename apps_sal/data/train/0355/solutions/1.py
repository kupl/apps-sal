class Solution:
    def findKthNumber(self, n, k):
        self.d = {}
        res = 1
        k -= 1
        while k > 0:
            # calculate how many numbers between current value and current value + 1
            count = self.countNumber(res, res + 1, n)
            if k >= count:
                #result >= res +1
                k -= count
                res += 1
            else:
                #res*10 <= result < res + 1
                k -= 1
                res *= 10
        return res

    def countNumber(self, l, r, maxValue):
        if l > maxValue:
            return 0
        if (l, r) in self.d:
            return d[(l, r)]
        res = min(maxValue + 1, r) - l
        l *= 10
        r *= 10
        res += self.countNumber(l, r, maxValue)
        self.d[(l, r)] = res
        return res

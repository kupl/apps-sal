class Solution:

    @staticmethod
    def compute_power(x, d={}):
        if x in d:
            return d[x]
        (xcopy, steps) = (x, 0)
        while x != 1 and x not in d:
            x = 3 * x + 1 if x % 2 else x // 2
            steps += 1 + d[x] if x in d else 1
        d[xcopy] = steps
        return steps

    def getKth(self, lo, hi, k):
        vals = list(range(lo, hi + 1))
        vals.sort(key=lambda x: self.compute_power(x))
        return vals[k - 1]

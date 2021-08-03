class Solution:
    def getKth(self, lo, hi, k):
        dic = {}
        for n in range(lo, hi + 1):
            steps = self.countStep(n)
            dic[n] = steps
        return sorted(dic.items(), key=lambda x: (x[1], x[0]))[k - 1][0]

    def countStep(self, m):
        step = 0
        while m != 1:
            if m % 2 == 0:
                m //= 2
            else:
                m = m * 3 + 1
            step += 1
        return step

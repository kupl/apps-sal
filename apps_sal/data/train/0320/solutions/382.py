class Solution:
    def minOperations(self, a: List[int]) -> int:
        res = [0]
        while True:
            self.checkOdd(a, res)
            end = self.checkDivide(a)
            if end:
                break
            else:
                res[0] += 1
        return res[0]

    def checkOdd(self, a, res):
        for i in range(len(a)):
            if a[i] % 2 != 0:
                a[i] -= 1
                res[0] += 1

    def checkDivide(self, a):
        flg = True
        for i in range(len(a)):
            if a[i] > 0:
                a[i] /= 2
                flg = False
        return flg

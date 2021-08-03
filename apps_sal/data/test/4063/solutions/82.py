n = int(input())
dn = list(map(int, input().split()))


class Solution:
    def __init__(self, n, dn):
        self.n = n
        self.dn = dn

    def __reverse(self):
        self.dn.sort()
        return self.dn

    def answer(self):
        self.dn = self.__reverse()
        a = self.dn[self.n // 2 - 1]
        b = self.dn[self.n // 2]
        print((b - a))


conditions = Solution(n, dn)
conditions.answer()

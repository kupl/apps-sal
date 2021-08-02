n, m, x = list(map(int, input().split()))
am = list(map(int, input().split()))


class Solution:
    def __init__(self, n, m, x, am):
        self.n = n
        self.m = m
        self.x = x
        self.am = am

    def __make_list(self):
        list_n = [0] * n
        for i in self.am:
            list_n[i - 1] = 1
        return list_n

    def answer(self):
        list_n = self.__make_list()
        print((min(sum(list_n[:self.x - 1]), sum(list_n[x - 1:]))))


conditions = Solution(n, m, x, am)
conditions.answer()

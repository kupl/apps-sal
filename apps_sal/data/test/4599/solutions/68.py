n = int(input())
an = list(map(int, input().split()))


class Solution:
    def __init__(self, n, an):
        self.n = n
        self.an = an

    @staticmethod
    def __reverse_an():
        r_an = sorted(an, reverse=True)
        return r_an

    def answer(self):
        r_an = self.__reverse_an()
        ans = 0
        for index, r_ai in enumerate(r_an):
            if index % 2 == 0:
                ans += r_ai
            else:
                ans -= r_ai
        print(ans)


conditions = Solution(n, an)
conditions.answer()

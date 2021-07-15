k, n = map(int, input().split())
an = list(map(int, input().split()))


class Solution:
    def __init__(self, k, n, an):
        self.k = k
        self.n = n
        self.an = an

    @staticmethod
    def __append_first():
        an.append(k + an[0])
        new_an = an
        return new_an

    def answer(self):
        new_an = self.__append_first()
        max_length = 0
        for i in range(n):
            max_length = max(max_length, new_an[i + 1] - new_an[i])
        print(k - max_length)


conditions = Solution(k, n, an)
conditions.answer()

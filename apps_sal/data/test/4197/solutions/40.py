n = int(input())
an = list(map(int, input().split()))


class Solution:
    values = [i for i in range(1, n + 1)]

    def __init__(self, n, an):
        self.n = n
        self.an = an

    def answer(self):
        d = dict(zip(self.an, Solution.values))
        for i in range(1, n + 1):
            print(d[i], end=' ')


conditions = Solution(n, an)
conditions.answer()

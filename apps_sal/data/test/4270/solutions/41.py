n = int(input())
vn = sorted(list(map(int, input().split())))


class Solution:
    def __init__(self, n, vn):
        self.n = n
        self.vn = vn

    def answer(self):
        ans = vn[0]
        for i in range(1, self.n):
            ans = (ans + self.vn[i]) / 2
        print(ans)


conditions = Solution(n, vn)
conditions.answer()


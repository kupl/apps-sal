(n, k) = list(map(int, input().split()))


class Solution:

    def __init__(self, n, k):
        self.n = n
        self.k = k

    def answer(self):
        self.n = self.n % self.k
        abs_n_minus_k = abs(self.n - self.k)
        ans = self.n
        if self.n % self.k == 0:
            ans = 0
        else:
            while abs_n_minus_k < self.n:
                self.n = abs_n_minus_k
                abs_n_minus_k = abs(self.n - self.k)
                ans = self.n
        print(ans)


conditions = Solution(n, k)
conditions.answer()

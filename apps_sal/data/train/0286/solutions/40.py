class Solution:
    def getProbability(self, balls: List[int]) -> float:

        total = sum(balls)

        def factorial(n):
            if n == 0:
                return 1
            if n < 3:
                return n
            return n * factorial(n - 1)

        self.match = 0
        self.total = 0

        def helper(p, left1, left2, cnt1, cnt2, per1, per2):
            if left1 == 0 and left2 == 0:
                self.total += per1 * per2
                self.match += per1 * per2 * (cnt1 == cnt2)
            elif left1 >= 0 and left2 >= 0:
                for k in range(balls[p] + 1):
                    helper(p + 1, left1 - k, left2 - balls[p] + k, cnt1 + (k > 0), cnt2 + (balls[p] - k > 0), per1 / factorial(k), per2 / factorial(balls[p] - k))

        helper(0, total // 2, total // 2, 0, 0, factorial(total // 2), factorial(total // 2))
        return self.match / self.total

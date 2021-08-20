class Solution:

    def minDays(self, n: int) -> int:
        memo = {}

        def check(num_orange, days_left):
            if days_left <= 0:
                return False
            if num_orange == 1:
                return True
            t = (num_orange, days_left)
            if t in memo:
                return memo[t]
            one = check(num_orange - 1, days_left - 1)
            two = three = False
            if num_orange % 2 == 0:
                two = check(num_orange // 2, days_left - 1)
            if num_orange % 3 == 0:
                three = check(num_orange // 3, days_left - 1)
            memo[t] = one or two or three
            return memo[t]
        for i in range(1, 50):
            if check(n, i):
                return i

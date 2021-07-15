import sys
class Solution():
    mem = dict()

    def classy_Numbers(self):
        T = int(sys.stdin.readline().strip())
        self.queries = []
        for t in range(T):
            left, right = list(map(int, sys.stdin.readline().strip().split()))
            print(self.dp(right, 3) - self.dp(left-1, 3))

    def dp(self, target, limit):
        num_digits = len(str(target))
        if (target, limit) in self.mem:
            return self.mem[(target, limit)]
        if limit == 0:
            return 1
        if num_digits <= limit:
            return target + 1

        top_digit = target // (10 ** (num_digits-1))
        res = target % (10 ** (num_digits-1))
        ret = self.dp(res, limit-1) \
                + max(top_digit-1, 0) * self.dp(10**(num_digits-1)-1, limit-1) \
                + self.dp(10**(num_digits-1)-1, limit)
        self.mem[(target, limit)] = ret
        return ret

sol = Solution()
sol.classy_Numbers()
# print(sol.dp(1, 3))
# print(sol.dp(1234, 4, 3))
# print(sol.dp(12345, 5, 3))


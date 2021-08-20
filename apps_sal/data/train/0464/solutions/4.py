class Solution:

    def minOperations(self, n: int) -> int:
        sum_out = None
        if n % 2 == 1:
            l = int(n / 2)
            num_ops = n - 1
            sum_out = 0
            for i in range(l):
                sum_out += num_ops
                num_ops -= 2
        elif n % 2 == 0:
            num_ops = n - 1
            l = int(n / 2)
            sum_out = 0
            for i in range(l):
                sum_out += num_ops
                num_ops -= 2
        return sum_out

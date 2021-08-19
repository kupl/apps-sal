class Solution:
    def countDigitOne(self, n):
        ones, wei = 0, 1
        while wei <= n:
            m = int(n / wei) % 10  # 求某位数字

            if m > 1:
                ones += (int(n / wei / 10) + 1) * wei
            elif m == 1:
                ones += (int(n / wei / 10)) * wei + (n % wei) + 1
            else:
                ones += (int(n / wei / 10)) * wei
            wei *= 10
        return int(ones)

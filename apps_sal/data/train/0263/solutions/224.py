class Solution:

    def knightDialer(self, n: int) -> int:
        w = [1]
        x = [1]
        y = [1]
        z = [1]
        for i in range(n - 1):
            w_n = 2 * x[-1]
            x_n = w[-1] + 2 * y[-1]
            y_n = x[-1] + z[-1]
            z_n = 2 * y[-1]
            w.append(w_n)
            x.append(x_n)
            y.append(y_n)
            z.append(z_n)
        return (w[-1] + 2 * x[-1] + 4 * y[-1] + 2 * z[-1] + (1 if n == 1 else 0)) % (10 ** 9 + 7)

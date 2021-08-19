import os
from io import BytesIO, StringIO
#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

DEBUG = False
debug_print = print if DEBUG else lambda *x, **y: None


def input_as_list():
    return list(map(int, input().split()))


def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()


def main():
    mod = 1000000007

    def modmul(x, y):
        return (x * y) % mod

    def row(m, i, n=3):
        return m[n * i:n * (i + 1)]

    def col(m, i, n=3):
        return m[i::n]

    def vecmul(u, v):
        s = 0
        for i, j in zip(u, v):
            s += (i * j) % (mod - 1)
        return s % (mod - 1)

    def matmul(a, b, n=3):
        out = []
        for i in range(n * n):
            r, c = divmod(i, n)
            out.append(vecmul(row(a, r), col(b, c)))
        return out

    def matadd(a, b, n=3):
        out = []
        for i in range(n * n):
            out.append((a[i] + b[i]) % (mod - 1))
        return out

    def matpow(m, p, n=3):
        bs = str(bin(p)).lstrip('0b')
        out = [0] * (n * n)
        out[0::n + 1] = [1] * n
        for b in reversed(bs):
            if b == '1':
                out = matmul(out, m)
            m = matmul(m, m)
        return out

    def brute_force(n, f1, f2, f3, c):
        i = 3
        while i < n:
            i += 1
            f4 = pow(c, 2 * i - 6, mod) * f1 * f2 * f3 % mod
            f1, f2, f3 = f2, f3, f4
        return f3

    def solve(n, f1, f2, f3, c):
        f = [f1, f2, f3]
        g = [modmul(c, f[0]), modmul(c * c, f[1]), modmul(c * c * c, f[2])]
        mat = [1, 1, 1, 1, 0, 0, 0, 1, 0]
        mat_n = matpow(mat, n - 3)
        g_n = (pow(g[2], mat_n[0], mod)
               * pow(g[1], mat_n[1], mod)
               * pow(g[0], mat_n[2], mod)) % mod
        c_n = pow(c, n, mod)
        c_n_inv = pow(c_n, mod - 2, mod)
        f_n = modmul(g_n, c_n_inv)
        return f_n

    def solve_from_stdin():
        i = input_as_list()
        print(solve(*i))

    def test():
        import random
        sample = [random.randrange(4, 99) for _ in range(5)]
        sample = [2, 2, 2, 2]
        print(*sample)
        for i in range(4, 200):
            print(i, *sample)
            print(solve(i, *sample))
            print(brute_force(i, *sample))
            print()

    solve_from_stdin()


main()

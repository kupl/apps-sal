import sys
in1 = sys.stdin.readlines()
N = int(in1[0])
'\n0 + 0 = 0\n0 x 0 = 0\n\n1 + 0 = 1\n1 x 0 = 1\n\n2 + 0 = 2\n2 x 0 = 2\n1 + 1 = 2\n1 x 1 = 0\n\n3 + 0 = 3\n3 x 0 = 3\n2 + 1 = 3\n2 x 1 = 3\n'
p = 10 ** 9 + 7


def f(n):
    if n in d:
        return d[n]
    d[n] = f(n // 2) + f((n - 1) // 2) + f((n - 2) // 2)
    return d[n]


d = {0: 1, 1: 2}
print(f(N) % p)

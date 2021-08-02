from itertools import chain
n = int(input())
def p(i): return "*" * ((n - i + 1) // 2) + "D" * i + "*" * ((n - i + 1) // 2)


print("\n".join(p(i) for i in chain(range(1, n + 1, 2), range(n - 2, 0, -2))))

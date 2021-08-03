nn = 2002002
P = 10**9 + 7
fa = [1] + [0] * nn
for i in range(nn):
    fa[i + 1] = fa[i] * (i + 1) % P


def f(a, b): return fa[a + b + 2] * pow(fa[a + 1] * fa[b + 1], P - 2, P) % P - 1


r1, c1, r2, c2 = map(int, input().split())
print((f(r2, c2) - f(r2, c1 - 1) - f(r1 - 1, c2) + f(r1 - 1, c1 - 1)) % P)

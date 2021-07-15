nn = 2002002
P = 10**9+7
fa = [1]
for i in range(1, nn): fa.append(fa[-1] * i % P)
f = lambda a, b: fa[a+b+2] * pow(fa[a+1] * fa[b+1], P-2, P) % P - 1
r1, c1, r2, c2 = map(int, input().split())
print((f(r2, c2) - f(r2, c1-1) - f(r1-1, c2) + f(r1-1, c1-1)) % P)

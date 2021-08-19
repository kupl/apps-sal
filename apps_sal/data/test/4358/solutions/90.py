a = int(input())
g = [int(input()) for _ in range(a)]
ma = max(g)
del g[g.index(ma)]
print(int(sum(g) + ma / 2))

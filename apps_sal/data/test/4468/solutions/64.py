N, T, *t = map(int, open(0).read().split())
ans = sum(y - x if y - x < T else T for x, y in zip(t[:N - 1], t[1:])) + T
print(ans)

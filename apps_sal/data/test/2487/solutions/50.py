N, *UV = map(int, open(0).read().split())

ans = N * (N + 1) * (N + 2) // 6
for u, v in zip(*[iter(UV)] * 2):
    if v < u:
        u, v = v, u
    ans -= u * (N - v + 1)

print(ans)

(N, *UV) = [int(_) for _ in open(0).read().split()]
ans = N * (N + 1) * (N + 2) // 6
for (u, v) in zip(UV[::2], UV[1::2]):
    if v > u:
        (u, v) = (v, u)
    ans -= v * (N + 1 - u)
print(ans)

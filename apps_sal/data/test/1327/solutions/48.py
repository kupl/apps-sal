(N, M) = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(2 ** 3):
    sign = [(-1) ** (i >> j & 1) for j in range(3)]
    (s, t, u) = sign
    xyz.sort(key=lambda x: s * x[0] + t * x[1] + u * x[2], reverse=True)
    (s, t, u) = (0, 0, 0)
    for (x, y, z) in xyz[:M]:
        s += x
        t += y
        u += z
    ans = max(ans, abs(s) + abs(t) + abs(u))
print(ans)

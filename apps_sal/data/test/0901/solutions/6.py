n, m = list(map(int, input().split()))

bad = 0
for _ in range(m):
    v = [0] * (n + 1)
    ok = 0
    for u in [int(i) for i in input().split()[1:]]:
        au = abs(u)
        su = 1 if u < 0 else 2
        v[au] |= su
        if v[au] == 3: ok = 1
    if not ok: bad = 1

print("YES" if bad else "NO")

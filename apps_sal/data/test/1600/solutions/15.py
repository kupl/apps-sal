n = int(input())
hs = list(map(int, input().split()))
max_h = 0
rs = []
max_hs = [0] * n
for i, h in enumerate(hs):
    rs.append((h, i))
    max_h = max(max_h, h)
    max_hs[i] = max_h
rs.sort()
p, r = 0, -1
ans = 0
while r < n - 1:
    nh, nr = rs[p]
    if r >= nr:
        p += 1
    else:
        r = nr
        p += 1
        while r < n - 1:
            nh, nr = rs[p]
            if nh >= max_hs[r]:
                break
            r = max(r, nr)
            p += 1
        ans += 1
print(ans)


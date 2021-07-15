digs = list(map(int, input()))

l, r = min(digs[:3], digs[3:], key=sum), max(digs[:3], digs[3:], key=sum)

ans = 0
while sum(r) - sum(l) > 0:
    if 9 - min(l) >= max(r):
        diff = 9 - min(l)
        l[l.index(min(l))] = 9
    else:
        diff = max(r)
        r[r.index(max(r))] = 0
    ans += 1

print(ans)


(n, k) = map(int, input().split())
(*a,) = map(int, input().split())
d = {}
ans = 0
for i in a:
    (x, j, tmp1, tmp2) = (i, 2, [], [])
    while j * j <= i:
        c = 0
        while x % j == 0:
            c += 1
            x //= j
        if c % k:
            tmp2.append((j, k - c % k))
            tmp1.append((j, c % k))
        j += 1
    if x > 1:
        tmp1.append((x, 1))
        tmp2.append((x, k - 1))
    (tmp1, tmp2) = (tuple(tmp1), tuple(tmp2))
    ans += d.get(tmp2, 0)
    d[tmp1] = d.get(tmp1, 0) + 1
print(ans)

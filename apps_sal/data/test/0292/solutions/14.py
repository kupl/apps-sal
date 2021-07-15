h, n = list(map(int, input().split()))
h -= 1
n -= 1
l = 0
r = 2 << h
ll = True
ans = 0
i = 0
while r - l > 1:
    m = (l + r) // 2
    if ll == (n < m):
        ans += 1
    else:
        ans += 1 << (h - i + 1)
    if n < m:
        r = m
        ll = False
    else:
        l = m;
        ll = True
    i += 1
print(ans)


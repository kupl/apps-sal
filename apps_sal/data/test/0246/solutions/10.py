(n, s) = map(int, input().split())
l = 1
r = n + 1
while r > l + 1:
    m = (l + r) // 2
    line = str(m)
    if m - sum((int(k) for k in line)) >= s:
        r = m
    else:
        l = m
line = str(l)
if l - sum((int(k) for k in line)) >= s:
    r = l
print(max(n - r + 1, 0))

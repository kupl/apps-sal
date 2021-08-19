(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
(x, y) = (0, 0)
(s1, s2) = (a[0], b[0])
while x != n or y != m:
    if s1 == s2:
        (x, y) = (x + 1, y + 1)
        if x == n and y == m:
            break
        (s1, s2) = (a[x], b[y])
        ans += 1
    elif s1 < s2:
        x += 1
        s1 += a[x]
    else:
        y += 1
        s2 += b[y]
print(ans + 1)

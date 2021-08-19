(n, p) = map(int, input().split())
s = list(input())
r = [0] * p
ans = 0
if not (p == 2 or p == 5):
    (x, t) = (0, 1)
    for i in range(-1, -(n + 1), -1):
        x += int(s[i]) * t
        x %= p
        r[x] += 1
        t *= 10
        t %= p
    for i in r:
        if i >= 2:
            ans += i * (i - 1) // 2
    ans += r[0]
else:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i + 1
print(ans)

s = [int(i) for i in input().split()]
y = 0
for i in range(14):
    u = s[:]
    t = s[i]
    u[i] = 0
    ans = 0
    for c in range(14):
        u[c] += t // 14
        if (c - i - 1) % 14 < t % 14:
            u[c] += 1
        if u[c] % 2 == 0:
            ans += u[c]
    y = max(ans, y)
print(y)

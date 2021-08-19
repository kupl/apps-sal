s = input()
n = len(s)
(g, p) = (0, 0)
ans = 0
for i in range(n):
    if g == p:
        g += 1
        if s[i] == 'p':
            ans -= 1
    else:
        p += 1
        if s[i] == 'g':
            ans += 1
print(ans)

(n, s) = input().split()
n = int(n)
ans = 0
for i in range(n):
    (a, t, g, c) = (0, 0, 0, 0)
    for j in range(i, n):
        if s[j] == 'A':
            a += 1
        elif s[j] == 'T':
            t += 1
        elif s[j] == 'G':
            g += 1
        else:
            c += 1
        if a == t and g == c:
            ans += 1
print(ans)

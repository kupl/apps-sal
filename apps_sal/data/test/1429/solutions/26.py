(n, s) = input().split()
n = int(n)
ans = 0
for i in range(n):
    (c1, c2) = (0, 0)
    for j in range(i, n):
        if s[j] == 'A':
            c1 += 1
        elif s[j] == 'T':
            c1 -= 1
        elif s[j] == 'C':
            c2 += 1
        elif s[j] == 'G':
            c2 -= 1
        if c1 == c2 == 0:
            ans += 1
print(ans)

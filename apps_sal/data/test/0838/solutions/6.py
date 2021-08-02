n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    l = sum([1 for e in a[i] if e == 0])
    nl = m - l
    ans += (2**l - 1 - l) + (2**nl - 1 - nl)

for i in range(m):
    l = 0
    for j in range(n):
        if a[j][i] == 0:
            l += 1
    nl = n - l
    ans += (2**l - 1 - l) + (2**nl - 1 - nl)

print(ans + n * m)

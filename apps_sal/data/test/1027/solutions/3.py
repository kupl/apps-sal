b = list(map(int, input().split()))
n = 14
ans = 0
for i in range(n):
    a = b.copy()
    if a[i] == 0:
        continue
    x = a[i]
    a[i] = 0
    full = x // n
    xex = x % n
    for j in range(n):
        a[j] += full
    for j in range(xex):
        a[(i + j + 1) % n] += 1
    pot = 0
    for j in a:
        if j % 2 == 0:
            pot += j
    ans = max(ans, pot)
print(ans)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
out = 1e9 + 1
for i in range(n):
    good = True
    dc = {}
    dif = (((b[i] - a[0]) % m) + m) % m
    for j in range(n):
        if b[j] in dc:
            dc[b[j]] += 1
        else:
            dc[b[j]] = 1
    for j in range(n):
        if (a[j] + dif) % m in dc and dc[(a[j] + dif) % m] > 0:
            dc[(a[j] + dif) % m] -= 1
        else:
            good = False
            break
    if good:
        out = min(out, dif)
print(out)

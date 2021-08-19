(n, k, m) = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p.sort()
ans = 0
for i in range(n + 1):
    l = m
    for j in range(k):
        l -= p[j] * i
    if l < 0:
        break
    cr = i * k + i
    for j in range(k):
        if l < p[j]:
            break
        c = min(l // p[j], n - i)
        l -= p[j] * c
        cr += c
    ans = max(ans, cr)
print(ans)

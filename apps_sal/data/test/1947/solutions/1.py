(n, m, l) = list(map(int, input().split()))
res = []
tim = 0
a = list(map(int, input().split()))
i = 0
while i < n:
    while i < n and a[i] <= l:
        i += 1
    if i == n:
        break
    tim += 1
    while i < n and a[i] > l:
        i += 1
for i in range(m):
    s = input()
    if s == '0':
        res.append(str(tim))
        continue
    (w, p, d) = list(map(int, s.split()))
    p -= 1
    if a[p] > l:
        continue
    a[p] += d
    if a[p] <= l:
        continue
    if p > 0 and a[p - 1] > l and (p < n - 1) and (a[p + 1] > l):
        tim -= 1
    elif p > 0 and a[p - 1] > l or (p < n - 1 and a[p + 1] > l):
        continue
    else:
        tim += 1
s = '\n'.join(res)
print(s)

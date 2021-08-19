(m, v) = map(int, input().split())
a = [0 for i in range(3500)]
b = []
for i in range(m):
    (d, l) = map(int, input().split())
    b.append([d, l])
b.sort()
for i in b:
    d = i[0]
    l = i[1]
    if a[d] + l <= v:
        a[d] += l
    elif a[d] > v:
        a[d + 1] += l
    else:
        total = a[d] + l
        a[d] = v
        a[d + 1] += total - v
ans = 0
for i in a:
    ans += min(i, v)
print(ans)

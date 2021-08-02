m, v = map(int, input().split())
a = [0 for x in range(3500)]
b = []
for i in range(m):
    b.append(list(map(int, input().split())))
b.sort()
# print(b)
for i in b:
    d = i[0]
    l = i[1]
    if a[d] + l <= v:
        a[d] += l
    else:
        if a[d] > v:
            a[d + 1] += l
        else:
            total = a[d] + l
            a[d] = v
            a[d + 1] += total - v
ans = 0
for j in a:
    ans += min(j, v)
print(ans)

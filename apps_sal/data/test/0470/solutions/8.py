d = {}
l = list(map(int, input().split()))
s = sum(l)
for i in l:
    d[i] = d.get(i, 0) + 1
ans = s
for i in d:
    if 2 <= d[i]:
        ans = min(ans, s - i * min(3, d[i]))
print(ans)

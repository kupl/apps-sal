l, r = map(int, input().split())
a = []
if r - l > 2019:
    for i in range(l, l + 2019):
        for j in range(i + 1, min(r + 1, l + 2020)):
            a.append((i * j) % 2019)
else:
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            a.append((i * j) % 2019)
ans = min(a)
print(ans)

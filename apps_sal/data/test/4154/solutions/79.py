n, m = map(int, input().split())
x = []
y = []
for i in range(m):
    l, r = map(int, input().split())
    x.append(l)
    y.append(r)
ans = max(0, min(y) - max(x) + 1)
print(ans)

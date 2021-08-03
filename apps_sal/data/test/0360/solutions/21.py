n = int(input())
l = list()
r = list()
for i in range(n):
    x, y = list(map(int, input().split()))
    l.append(x)
    r.append(y)
k = int(input())
ans = 0
for i in range(n):
    if k <= r[i]:
        ans += 1
print(ans)

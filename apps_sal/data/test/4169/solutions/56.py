n, m = map(int, input().split())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort(key=lambda x: x[0])
ans = 0
count = 0
for i in range(n):
    k = min(m - count, l[i][1])
    count += k
    ans += k * l[i][0]
print(ans)

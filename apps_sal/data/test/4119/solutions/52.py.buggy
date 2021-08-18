n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
if n >= m:
    print((0))
    return
x.sort()
l = []
for i in range(m - 1):
    l.append(x[i + 1] - x[i])
l.sort(reverse=True)
ans = x[m - 1] - x[0]
for i in range(n - 1):
    ans -= l[i]
print(ans)

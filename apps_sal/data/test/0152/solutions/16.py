n, m, k = list(map(int, input().split()))
x, s = list(map(int, input().split()))
k += 1
m += 1
a = [x] + [int(x) for x in input().split()]
b = [0] + [int(x) for x in input().split()]
c = [0] + [int(x) for x in input().split()]
d = [0] + [int(x) for x in input().split()]
fir = []
for i in range(m):
    fir.append([a[i], b[i]])
fir.sort(key=lambda x: x[1])
ans = n * x
for i in range(m):
    left = s - fir[i][1]
    if (left < 0): break
    while(d[k - 1] > left): k -= 1
    now = (n - c[k - 1]) * fir[i][0]
    ans = min(ans, now)
print(ans)

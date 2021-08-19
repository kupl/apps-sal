n = int(input())
a = list(map(int, input().split()))
l = [i + a[i] for i in range(n)]
r = [i - a[i] for i in range(n)]
x = {}
y = {}
for i in range(n):
    x[l[i]] = 0
    y[l[i]] = 0
    y[r[i]] = 0
for i in range(n):
    x[l[i]] += 1
    y[r[i]] += 1
ans = 0
for i in set(x.keys()):
    ans += x[i] * y[i]
print(ans)

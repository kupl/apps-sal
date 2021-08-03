# yeh dil maange more
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
c = [0] * (n + 1)
d = [0] * (m + 1)
x = int(input())

for i in range(1, n + 1):
    a[i] = a[i - 1] + a[i]
    c[i] = a[i]
    for j in range(1, i):
        c[i - j] = min(c[i - j], a[i] - a[j])
# print(c)
for i in range(1, m + 1):
    b[i] = b[i - 1] + b[i]
    d[i] = b[i]
    for j in range(1, i):
        d[i - j] = min(d[i - j], b[i] - b[j])
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if c[i] * d[j] <= x:
            ans = max(ans, i * j)
print(ans)

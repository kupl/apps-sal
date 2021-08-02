n, x = map(int, input().split())
a = list(map(int, input().split()))
t = min(a)
if t != 0:
    for i in range(n):
        a[i] -= t - 1
i = x - 1
c = 0
while a[i] != 0:
    a[i] -= 1
    c += 1
    i -= 1
    if i == -1:
        i = n - 1
a[i] += c + max(t - 1, 0) * n
for i in a:
    print(i, end=' ')

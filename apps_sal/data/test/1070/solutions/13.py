n, k = map(int, input().split())
a = list(map(int, input().split()))
d = a[0]
s = 1
m = 1

for i in range(1, n):
    if d != a[i]:
        s += 1
    else:
        s = 1
    d = a[i]
    if s > m:
        m = s
print(m)

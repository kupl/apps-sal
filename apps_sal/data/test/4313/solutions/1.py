n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
a = []
for i in range(n):
    b = v[i] - c[i]
    a.append(b)
d = 0
for j in range(n):
    if a[j] > 0:
        d += a[j]
print(d)

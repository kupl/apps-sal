(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = []
x = 0
a.sort()
b.sort()
for t in range(n):
    if a[t] > 0:
        d.append(a[t] * b[-1])
    else:
        d.append(a[t] * b[0])
d.sort()
print(d[-2])

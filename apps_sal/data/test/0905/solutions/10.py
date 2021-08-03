n, s = list(map(int, input().split()))
x = []
y = []
maximum = 0
k = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    x.append(a)
    y.append(b)
for i in range(n):
    if s > x[i] and 100 - y[i] > maximum and y[i] > 0:
        maximum = 100 - y[i]
    if s < x[i]:
        k += 1
    if s == x[i] and y[i] > 0:
        k += 1
if k == n:
    print(-1)
else:
    print(maximum)

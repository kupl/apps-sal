n, r = map(int, input().split())
x = list(map(int, input().split()))
y = []
for i in range(n):
    s = []
    for j in range(i):
        if abs(x[i] - x[j]) < 2 * r + 0.0000001:
            s.append(j)
    max = r
    for j in s:
        if (4 * r * r - (x[i] - x[j])**2)**0.5 + y[j] > max:
            max = (4 * r * r - (x[i] - x[j])**2)**0.5 + y[j]
    y.append(max)
for i in y:
    print(i, end=' ')

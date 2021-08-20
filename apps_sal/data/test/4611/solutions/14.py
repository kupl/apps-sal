N = int(input())
t = [0] * (N + 1)
x = [0] * (N + 1)
y = [0] * (N + 1)
for i in range(N):
    (t[i + 1], x[i + 1], y[i + 1]) = map(int, input().split())
f = True
for i in range(N):
    dt = t[i + 1] - t[i]
    dist = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    if dt < dist:
        f = False
    if dist % 2 != dt % 2:
        f = False
print('Yes' if f else 'No')

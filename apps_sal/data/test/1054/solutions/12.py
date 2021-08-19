n = int(input())
x = []
y = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    x.append(a)
    y.append(b)
x.sort()
y.sort()
print(max(x[-1] - x[0], y[-1] - y[0]) ** 2)

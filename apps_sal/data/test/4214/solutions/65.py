import math
n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    (x[i], y[i]) = list(map(int, input().split()))
q = 2
for i in range(2, n):
    q *= i
s = 0.0
for i in range(n - 1):
    for j in range(i, n):
        s += math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) * q
f = math.factorial(n)
print(s / f)

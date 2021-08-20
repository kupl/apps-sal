import sys
import math
(n, a, b) = map(int, input().split())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    (u, v) = map(int, input().split())
    x[i] = u
    y[i] = v
m = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if x[i] + x[j] <= a and max(y[i], y[j]) <= b or (x[i] + y[j] <= a and max(y[i], x[j]) <= b) or (y[i] + x[j] <= a and max(x[i], y[j]) <= b) or (y[i] + y[j] <= a and max(x[i], x[j]) <= b) or (x[i] + x[j] <= b and max(y[i], y[j]) <= a) or (x[i] + y[j] <= b and max(y[i], x[j]) <= a) or (y[i] + x[j] <= b and max(x[i], y[j]) <= a) or (y[i] + y[j] <= b and max(x[i], x[j]) <= a):
                if m < x[i] * y[i] + x[j] * y[j]:
                    m = x[i] * y[i] + x[j] * y[j]
print(m)

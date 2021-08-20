import math
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = 0
b = 0
for i in range(0, n, 1):
    a += (p[i] - 1) * math.factorial(n - i - 1)
    b += (q[i] - 1) * math.factorial(n - i - 1)
    for j in range(i + 1, n, 1):
        if p[j] > p[i]:
            p[j] -= 1
        if q[j] > q[i]:
            q[j] -= 1
print(abs(a - b))

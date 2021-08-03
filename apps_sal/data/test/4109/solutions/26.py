import numpy as np
n, m, x = list(map(int, input().split()))
c = []
a = []

for i in range(n):
    stdIn = list(map(int, input().split()))
    c.append(stdIn[0])
    a.append(stdIn[1:])
flag = 0
ans = sum(c)
for i in range(2**n):
    result = np.array([0] * m)
    price = 0
    for j in range(n):
        if((i >> j) & 1):
            result += a[j]
            price += c[j]
    if (len(result[result < x]) == 0):
        ans = min(ans, price)
        flag = 1
print(ans if flag != 0 else -1)

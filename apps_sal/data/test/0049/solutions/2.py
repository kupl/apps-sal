import math
n = int(input())
a = [9]
for i in range(2, 20):
    a.append(10 ** i - 10 ** (i - 1))
b = [0]
for i in range(1, 20):
    b.append(b[-1] + i * a[i - 1])
for i in range(20):
    if n <= b[i]:
        break
p = b[i - 1]
k = n - p
ans = 10 ** (i - 1) - 1 + math.ceil(k / i)
if k % i == 0:
    print(('0' + str(ans))[i])
else:
    print(('0' + str(ans))[k % i])

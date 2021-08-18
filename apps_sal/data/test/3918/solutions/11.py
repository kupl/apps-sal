
import math

n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = []
for i in range(n):
    x.append(int(math.fabs(a[i] - b[i])))

k = k1 + k2
while k > 0:
    max_num = 0
    idx = -1
    for i in range(n):
        if x[i] > max_num:
            max_num = x[i]
            idx = i
    if idx == -1:
        break
    x[idx] -= 1
    k -= 1

ret = 0
for i in range(n):
    ret += x[i] * x[i]
if k % 2 == 1:
    ret += 1
print(ret)

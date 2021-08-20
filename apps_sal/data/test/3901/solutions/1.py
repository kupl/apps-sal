import math
n = int(input())
l1 = list(map(int, input().split()))
flag = -1
sz = n - l1.count(1)
if n - sz > 0:
    flag = sz
for j in range(n):
    if flag != -1:
        break
    if l1.count(1) > 0:
        flag = j + sz - 1
        break
    for i in range(n - 1):
        l1[i] = math.gcd(l1[i], l1[i + 1])
    l1.pop()
    n -= 1
print(flag)

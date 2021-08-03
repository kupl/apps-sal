import math
n, k = map(int, input().split())
_ = list(map(int, input().split()))
a = [0 for i in range(101)]
for i in _:
    a[i] += 1
k1 = math.ceil(max(a) / k) * k
s1 = 0
for i in a:
    if (i > 0):
        s1 += (k1 - i)
print(s1)

from collections import Counter as C
n = int(input())
a = list(map(int, input().split()))
l = C([i + a[i] for i in range(n)])
r = C([i - a[i] for i in range(n)])
b = 0
for i in l.keys():
    b += l[i] * r[i]
print(b)

import math
a = list(map(int, input().split()))
s = int(input())
for i in range(s):
    a[a.index(max(a))] = a[a.index(max(a))] * 2
print(sum(a))

import os
l = list(map(int, input().split()))
l.sort()
a = l[2] * 10 + l[1] + l[0]
print(a)

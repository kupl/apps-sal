import math


a = int(input())
s = [int(i) for i in input().split()]
ma = 0
i = 0
k = 0
while i < a:
    ma = max(ma, s[i])
    while ma > i + 1:
        i += 1
        ma = max(ma, s[i])
    i += 1
    k += 1
print(k)

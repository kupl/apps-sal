import sys
N = int(input())
A = list(map(int, input().split()))
d = {}
a = []
for i in A:
    if i in d:
        d[i] += 1
        if d[i] == 2:
            a.append(i)
            d[i] = 0
    else:
        d[i] = 1
a.sort()
if len(a) < 2:
    print(0)
else:
    print(a[-1] * a[-2])

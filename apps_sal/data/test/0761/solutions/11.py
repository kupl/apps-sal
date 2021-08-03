import math
n = int(input())
arr = list(map(int, input().split()))
cp = 0
cn = 0
for i in range(len(arr)):
    if arr[i] >= 0:
        cp += 1
    else:
        cn += 1
b = []
for i in range(len(arr)):
    b.append(abs(arr[i]))
m = min(b)
if n == 1:
    print(arr[0])
else:
    if cp > 0 and cn > 0:
        print(sum(b))
    else:
        nrt = 2 * (min(b))
        print(sum(b) - nrt)

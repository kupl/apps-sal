from math import *

n = int(input())

a = list(map(int, input().split(" ")))

tmp = 0

mx = 0

for i in a:
    if(i == 1):
        if(tmp == 0):
            tmp = 1
        else:
            tmp += 1
    else:
        tmp = 0
    mx = max(mx, tmp)
mx2 = 0

i = n - 1

while(a[i] != 0):
    mx2 += 1
    i -= 1
i = 0
while(a[i] != 0):
    mx2 += 1
    i += 1
print(max(mx2, mx))

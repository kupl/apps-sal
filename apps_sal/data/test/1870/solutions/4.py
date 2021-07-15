import sys, math
n,m = list(map(int, input().split()))
ctr = 1
z = list(map(int, input().split()))
for i in range(1, n):
    if z[i] - z[i - 1] <= m:
        ctr += 1
    else:
        ctr = 1
print(ctr)
    


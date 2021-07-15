# -*- coding: utf-8 -*-

n = int(input())
a = [int(x) for x in input().split()]

ret = [0,0]
sum = [0,0]

if a[0]==0:
    sum[0] = 1
    ret[0] = 1
    sum[1] = -1
    ret[1] = 1
elif a[0]>0:
    sum[0] = a[0]
    sum[1] = -1
    ret[1] = a[0]+1
else:
    sum[0] = 1
    ret[0] = -1*a[0]+1
    sum[1] = a[0]

for i in range(1,n):
    for j in range(2):
        if sum[j]*(sum[j]+a[i])<0:
            sum[j] += a[i]
        elif sum[j]+a[i]==0:
            if sum[j]>0:
                sum[j] = -1
            else:
                sum[j] = 1
            ret[j] += 1
        elif sum[j]+a[i]>0:
            ret[j] += sum[j]+a[i]+1
            sum[j] = -1
        else:
            ret[j] += -1*(sum[j]+a[i])+1
            sum[j] = 1

print((min(ret[0],ret[1])))


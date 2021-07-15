import sys
n,k=list(map(int,input().split()))
h=list(map(int,input().split()))

list.sort(h,reverse=True)

if k>=n:
    print('0')
    return

c=0
for i in range(k,n):
    c+=h[i]

print(c)


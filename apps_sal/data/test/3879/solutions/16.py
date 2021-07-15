__author__ = 'pxy'
n=int(input())
c=[int(i) for i in input().split()]
f=True
for j in range(n):
    while c[j] % 2 == 0:
        c[j]=c[j]// 2
    while c[j] % 3 == 0:
        c[j]=c[j]// 3
if(max(c)==min(c)):
    print('Yes')
else:
    print('No')

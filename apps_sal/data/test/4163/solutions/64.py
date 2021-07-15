a=[]
n=int(input())
for i in range(n):
    a.append(input().split())

f=False
i=0
while i < n-2 and f==False:
    if (a[i][0]==a[i][1] and
    a[i+1][0]==a[i+1][1] and
    a[i+2][0]==a[i+2][1]):
        f=True
    i=i+1
    
if f==False:
    print('No')
else:
    print('Yes')


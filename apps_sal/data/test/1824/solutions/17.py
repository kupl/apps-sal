n=int(input())
a=[input() for i in range(3)]
for i in range(3):
    a[i]=a[i].split()
for i in range(3):
    for j in range(len(a[i])):
        a[i][j]=int(a[i][j])
for i in a:
    i.sort()
er1=-1; er2=-1
for i in range(n-1):
    if i<n-1 and er1==-1 and a[0][i]!=a[1][i]:
        er1=a[0][i]
    if i<n-2 and er2==-1 and a[1][i]!=a[2][i]:
        er2=a[1][i]
if er1==-1: er1=a[0][n-1]
if er2==-1: er2=a[1][n-2]
print(er1)
print(er2)

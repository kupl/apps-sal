n = int(input())
arr = []
for i in range(n):
    arr.append([int(x) for x in input().split()])
if(n==1):
    print(1)
    return

ii,jj = 0,0
for i in range(n):
    for j in range(n):
        if(arr[i][j]==0):
            ii,jj = i,j

prr = []
qrr = []
for i in range(n):
    if(i==ii):
        qrr.append(sum(arr[i]))
    else:
        prr.append(sum(arr[i]))
for j in range(n):
    s = 0
    for i in range(n):
        s += arr[i][j]
    if(j==jj):
        qrr.append(s)
    else:
        prr.append(s)
s = 0
for i in range(n):
    s += arr[i][i]
if(ii==jj):
    qrr.append(s)
else:
    prr.append(s)
s = 0
for i in range(n):
    s += arr[i][n-i-1]
if(ii+jj==n-1):
    qrr.append(s)
else:
    prr.append(s)

if(len(prr)==prr.count(prr[0]))and(len(qrr)==qrr.count(qrr[0])):
    x = prr[0]-qrr[0]
    if(x>0):
        print(x)
    else:
        print(-1)
else:
    print(-1)

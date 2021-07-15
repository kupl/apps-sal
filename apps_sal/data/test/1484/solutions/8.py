input1 = input('').split(' ')
k = int(input1.pop())
n = int(input1.pop())
input2 = input('').split(' ')
lis11 = []
lis12 = []
lis21 = []
lis22 = []
lisk = []
long = 0
op = 1
for i in range(n):
    if i % 2 == 0:
        lis11.append(int(input2[i]))
    else:
        lis12.append(int(input2[i]))
tong = [0,1,k-1]
yi = [0,1,k-2]
for i in range((n+1)//2):
    if lis11[i] != -1:
        lis21.append(i)
        if len(lis21)>1:
            if (i-lis21[-2]) > long:
                long = i-lis21[-2]
    if (i>0) & (lis11[i]>0):
        if lis11[i-1] == lis11[i]:
            lisk.append(0)
for i in range(n//2):
    if lis12[i] != -1:
        lis22.append(i)
        if len(lis22)>1: 
            if (i-lis22[-2]) > long:
                long = i-lis22[-2]
    if (i>0) & (lis12[i]>0):
        if lis12[i-1] == lis12[i]:
            lisk.append(0)
for i in range(3,long+1):
    tong.append(int(yi[i-1])*(k-1)%998244353)
    yi.append((int(yi[i-1])*(k-2)+tong[i-1])%998244353)
if lis21:
    for i in range(lis21[0] - lis21[-1] + (n+1)//2 - 1):
        lisk.append(k-1)
    for i in range(1,len(lis21)):
        if lis11[lis21[i]] == lis11[lis21[i-1]]:
            lisk.append(tong[lis21[i]-lis21[i-1]])
        else:
            lisk.append(yi[lis21[i]-lis21[i-1]])
else:
    lisk.append(k)
    for i in range(1,(n+1)//2):
        lisk.append(k-1)
if lis22:
    for i in range(lis22[0] - lis22[-1] + n//2 - 1):
        lisk.append(k-1)
    for i in range(1,len(lis22)):
        if lis12[lis22[i]] == lis12[lis22[i-1]]:
            lisk.append(tong[lis22[i]-lis22[i-1]])
        else:
            lisk.append(yi[lis22[i]-lis22[i-1]])
else:
    lisk.append(k)
    for i in range(1,n//2):
        lisk.append(k-1)
if len(lisk) > 0:
    for i in range(len(lisk)):
            op = op * lisk[i] % 998244353
print(op)

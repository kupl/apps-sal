import math

nM=input().split(' ')
n = int(nM[0])
M = int(nM[1])

a = list(map(int,input().split(' ')))

carr = [0 for i in range(100)]

carr[a[0]-1]+=1
print('0',end=' ')

sum=a[0]
for i in range(1,len(a)):
    failed=0
    if sum+a[i] > M:
        A = sum+a[i]
        for itr in range(100,0,-1):
            if A - carr[itr-1]*itr > M:
                A-=carr[itr-1]*itr
                failed+=carr[itr-1]
                # print(A,itr,failed)
            else:
                failed+=math.ceil((A-M)/itr)
                # print('vade',failed)
                break
        print(failed,end=' ')
    else:
        print(failed, end=' ')
    
    sum+=a[i]
    carr[a[i]-1]+=1

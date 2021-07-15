N =int(input())
A= list(map(int,input().split()))
count=0
for i in range(N):
    if  A[i]%2 !=0:
        continue
    else:
        N =A[i]
        while N %2==0:
            N=N//2
            count+=1
print(count)


n=int(input())
lis=list(map(int,input().split()))
lis2=[]
for i in range(0,len(lis)-1):
    lis2.append(lis[i]+lis[i+1])
lis2.append(lis[len(lis)-1])
for i in lis2:
    print(i,end=' ')

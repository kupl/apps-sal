N=int(input())
D1=[""]*N
D2=[""]*N

for i in range(N):
    [D1[i],D2[i]]=list(map(int,input().split()))



flag=False
for i in range(0,N-2):
    if D1[i]==D2[i] and D1[i+1]==D2[i+1] and D1[i+2]==D2[i+2]:
        print('Yes')
        flag=True
        break


if flag==False:
    print('No')



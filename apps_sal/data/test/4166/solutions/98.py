N,M=map(int, input().split())
A=[list(map(int, input().split()))  for _ in range(M)]
A = sorted(A, reverse=False, key=lambda x: x[0])

if M==0:
    if N==3:
        print(100)
        return
    elif N==2:
        print(10)
        return        
    elif N==1:
        print(0)
        return

if N!=1 and A[0][0]==1 and A[0][1]==0:
    print(-1)
    return
i=1
j=len(A)
while i<j:
    if A[i][0]==A[i-1][0] and A[i][1]==A[i-1][1]:
        A.pop(i)
        j-=1
        continue
    elif A[i][0]==A[i-1][0] and A[i][1]!=A[i-1][1]:
        print(-1)
        return
    i+=1
ans=[None]*N

for i,j in A:
    ans[i-1]=j

for i in range(len(ans)):
    if ans[i]==None:
        if i==0:
            ans[i]=1
        else:
            ans[i]=0

print(''.join(map(str,ans)))

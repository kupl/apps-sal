N=int(input())
S=list(map(int,input().split()))
lenS=len(S)
T=[]
for i in range(1,N+1):
    T.append(abs(i-(N+1-i)))

T.sort()
S.sort()



for i in range(N):
    if T[i]!=S[i]:
        print((0))
        return


ans=1
nagasa=lenS//2
for i in range(nagasa):
    
    ans=(ans*2)%(10**9+7)

print(ans)




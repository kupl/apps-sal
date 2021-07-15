N=int(input())
S=[''.join(sorted(input())) for _ in range(N)]
ans=0
num=1
S.sort()
for i in range(1,N):
    if S[i-1]==S[i]:
        num+=1
    else:
        ans+=num*(num-1)//2
        num=1
ans+=num*(num-1)//2
print(ans)


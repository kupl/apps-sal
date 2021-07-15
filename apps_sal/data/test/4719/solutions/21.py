N=int(input())
S=[input() for _ in range(N)]

F = [[0]*N for _ in range(26)]

f1=lambda c: ord(c) - ord('a')
f2=lambda c: chr(c+97)


for i in range(N):
    for s in S[i]:
        F[f1(s)][i]+=1
        
ans=''
for i in range(26):
    t=min(F[i])
    if t!=0:
        ans+=t*f2(i)
print(ans)

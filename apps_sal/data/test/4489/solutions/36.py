N=int(input())
s=dict()
for _ in range(N):
    S=input()
    if S not in s:
        s[S]=0
    s[S]+=1
M=int(input())
for _ in range(M):
    t=input()
    if t in s:
        s[t]-=1
print((max(max(0,x) for x in list(s.values()))))


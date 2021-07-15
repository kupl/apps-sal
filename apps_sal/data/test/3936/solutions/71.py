N,S,T=open(0)
ans=3
i=1
if S[0]!=T[0]:
    ans*=2
    i*=2
while i<int(N):
    if S[i-1]==T[i-1]:
        ans*=2
    elif S[i]!=T[i]:
        ans*=3
    i+=1+(S[i]!=T[i])
print(ans%(10**9+7))

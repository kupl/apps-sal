S=input()
N=len(S)
s=''.join(list(reversed(S)))

T=S[0:int((N-1)/2)]
NT=len(T)
t=''.join(list(reversed(T)))

U=S[int((N+1)/2):N]
NU=len(U)
u=''.join(list(reversed(U)))

if S[0:int((N-1)/2)] == s[0:int((N-1)/2)] and T == t and U == u:
    print('Yes')
else:
    print('No')

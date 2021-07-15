N = int(input())
A = list(map(int, input().split()))
s = 0
S = [0]*N
for i, a in enumerate(A):
    s += a
    S[i] = s

t = S[-1]
ans = 10**20
j = 0
k = 2
for i in range(1,N-2):
    s = S[i]
    while abs(s-2*S[j+1]  ) < abs(s-2*S[j]  ): j+=1
    while abs(t-2*S[k+1]+s) < abs(t-2*S[k]+s): k+=1
    
    v = (S[j], s-S[j], S[k]-s, t-S[k])
    ans = min(ans, max(v)-min(v))
    
    #print(i,j,k, v)
print(ans)

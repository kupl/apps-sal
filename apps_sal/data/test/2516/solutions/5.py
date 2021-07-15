N, P = list(map(int, input().split()))
S = [int(i) for i in input()]
from collections import Counter
def solve(S,N,P):
    if P==2 or P==5:
        ans = 0
        for i in range(N):
            if S[i]%P==0:
                ans += i+1
        return ans
    cum = [0]*(N+1)
    mods = [0]*N
    mods[0] = 1
    for i in range(1,N):
        mods[i] = mods[i-1]*10%P
    for i in range(N):
        cum[i+1] = (cum[i]+S[N-1-i]*mods[i])%P
    c = Counter(cum)
    ans = 0
    for v in list(c.values()):
        ans += v*(v-1)//2
    return ans
print((solve(S,N,P)))


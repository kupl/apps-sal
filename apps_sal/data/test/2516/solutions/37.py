import sys
from collections import Counter

def ep(*params):
    print(*params,file=sys.stderr)

(N,P) = list(map(int,input().split()))
S = input().rstrip()

if 10%P == 0:
    ans = 0
    for i in range(N):
        if int(S[i])%P == 0:
            ans += i+1
    print(ans)
    return

ans = 0
d = [0]*(N+1)
cnt = [0]*P
ten = 1

for i in range(N-1,-1,-1):
    a = int(S[i]) * ten % P
    d[i] = (d[i+1]+a) % P
    ten *= 10
    ten %= P

#ep(d)

for i in range(N,-1,-1):
    ans += cnt[d[i]]
    cnt[d[i]] += 1;
    #ep(i,ans,cnt)
#ep(cnt)
print(ans)

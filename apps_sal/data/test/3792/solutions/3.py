import sys
readline = sys.stdin.readline

N, K = list(map(int, readline().split()))
S = [1 if s == 'b' else 0 for s in readline().strip()]
T = [1 if s == 'b' else 0 for s in readline().strip()]

diff = 0
for s, t in zip(S, T):
    if diff > K:
        break
    if s == t:
        diff <<= 1
    elif s == 1:
        diff = (diff << 1) - 1
    else:
        diff = (diff << 1) + 1

K = min(K, diff + 1)

ans = 0
cnt = 1
ans = 0
for s, t in zip(S, T):
    if cnt == K:
        ans += cnt
        continue
    if cnt == 1:
        if s == t:
            ans += cnt
        else:
            cnt += 1
            cnt = min(K, cnt)
            ans += cnt
        continue
    else:
        cnt *= 2
        if s == 1:
            cnt -= 1
        if t == 0:
            cnt -= 1
        cnt = min(K, cnt)
        ans += cnt
    
print(ans)


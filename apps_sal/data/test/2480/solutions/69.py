from collections import Counter

N, K = list(map(int, input().split()))
As = list(map(int, input().split()))

Ss = [0]
S = 0
for A in As:
    S += A-1
    S %= K
    Ss.append(S)

ans = 0
cnt = Counter()
for i in range(N+1):
    ans += cnt[Ss[i]]
    cnt[Ss[i]] += 1
    if i >= K-1:
        cnt[Ss[i-K+1]] -= 1

print(ans)


from collections import defaultdict

N, P = list(map(int, input().split()))
S = input().strip()[::-1]

if P in [2, 5]:
    ans = 0
    for r in range(N):
        if int(S[r]) % P == 0:
            ans += N - r
    print(ans)
    return

cum = [0] * (N + 1)
for i in range(N):
    now = int(S[i]) * pow(10, i, P)
    cum[i + 1] = (cum[i] + now) % P

cnt = defaultdict(int)
for _cum in cum:
    cnt[_cum] += 1

ans = 0
for k, v in list(cnt.items()):
    ans += v * (v - 1) // 2

print(ans)


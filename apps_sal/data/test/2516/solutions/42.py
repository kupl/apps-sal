N, P = list(map(int, input().split()))
S = input().strip()[::-1]

if P in [2, 5]:
    ans = 0
    for r in range(N):
        if int(S[r]) % P == 0:
            ans += N - r
    print(ans)
    return

d = [0] * (N + 1)
ten = 1
for i in range(N):
    a = int(S[i]) * ten % P
    d[i + 1] = (d[i] + a) % P
    ten *= 10
    ten %= P

cnt = [0] * P
ans = 0
for i in range(N + 1):
    ans += cnt[d[i]]
    cnt[d[i]] += 1

print(ans)

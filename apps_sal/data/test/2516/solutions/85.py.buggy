from collections import Counter

N, P = map(int, input().split())
S = input()

if P == 2:
    ret = 0
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ret += i + 1
    print(ret)
    return

if P == 5:
    ret = 0
    for i in range(N):
        if int(S[i]) % 5 == 0:
            ret += i + 1
    print(ret)
    return

mods = [0] * (N + 1)

for i in reversed(range(N)):
    mods[i] = (mods[i + 1] + pow(10, N - i - 1, P) * int(S[i])) % P

cnt = Counter(mods)
ans = 0
for i in cnt:
    ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)

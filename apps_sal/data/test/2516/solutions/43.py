# coding: utf-8
N, P = map(int, input().split())
S = input()
ans = 0
if P == 2:
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ans += i + 1
elif P == 5:
    for i in range(N):
        if int(S[i]) == 0 or int(S[i]) == 5:
            ans += i + 1
else:
    cnt = [0 for _ in range(P)]
    cnt[0] = 1
    bai = 1
    v = 0
    for i in range(N)[::-1]:
        v = (v + int(S[i]) * bai) % P
        bai *= 10
        bai %= P
        cnt[v] += 1
    for i in range(P):
        ans += ((cnt[i] - 1) * cnt[i]) // 2
print(ans)

N, K = map(int, input().split())
A = list(map(int, input().split()))
D, E = [], []
zcnt, scnt, fcnt = 0, 0, 0
for i in A:
    if i == 0:
        zcnt += 1
        D.append(0)
    elif i > 0:
        D.append(i)
        scnt += 1
    else:
        E.append(i)
        fcnt += 1
mod = 10**9 + 7
ans = 1
# 全て使う場合は問答無用でかける
if K == N:
    for i in A:
        ans *= i
        ans %= mod
    print(ans)
    return
# マイナスを奇数個絶対かける→確実に答えはマイナス
if K % 2 == 1 and max(A) < 0:
    A = sorted(A)[::-1]
    for i in range(K):
        ans *= A[i]
        ans %= mod
    print(ans)
    return
# 絶対0をかけなきゃいけない
if K > scnt + fcnt:
    print(0)
    return
D, E = sorted(D)[::-1], sorted(E)
# print(D,E)
ans = 1
cnt = 0
a, b = 0, 0
while K - cnt > 1:
    if a + 1 <= len(D) - 1 and b + 1 <= len(E) - 1:
        d, e = D[a] * D[a + 1], E[b] * E[b + 1]
        if d > e:
            ans *= D[a]
            a += 1
            cnt += 1
            ans %= mod
        else:
            ans *= e
            b += 2
            ans %= mod
            cnt += 2
    elif a + 1 <= len(D) - 1:
        d = D[a] * D[a + 1]
        ans *= D[a]
        a += 1
        cnt += 1
        ans %= mod
    elif b + 1 <= len(E) - 1:
        e = E[b] * E[b + 1]
        ans *= e
        b += 2
        cnt += 2
        ans %= mod

if K - cnt == 1:
    Z = []
    if a != scnt:
        Z.append(D[a])
    if b != fcnt:
        Z.append(E[-1])
    if 0 in A:
        Z.append(0)
    ans *= max(Z)
    ans %= mod
print(ans)

import math
N, K = map(int, input().split())
x = list(map(int, input().split()))
for i in range(N):
    if x[i] == 0:
        p, m = i, i + 1
        break
    elif x[i] > 0:
        p, m = i, i
        break

if (x[0] < 0) and (x[-1] > 0):
    pls = x[p:]
    mns = x[:m]
    ans = math.inf

    for i in range(len(pls)):
        if i < K - 1:
            if pls[0] == 0:
                n = K - i
            else:
                n = K - i - 1
            if len(mns) >= n:
                tmp = 2 * abs(mns[-n]) + pls[i]
                ans = min(ans, tmp)
        if i == K - 1:
            ans = min(ans, pls[i])
            break

    for i in range(len(mns)):
        m = len(mns) - i
        if m < K:
            if pls[0] == 0:
                n = K - m
            else:
                n = K - m - 1
            if len(pls) > n:
                tmp = 2 * pls[n] + abs(mns[-m])
                ans = min(ans, tmp)
        if m == K:
            ans = min(ans, abs(mns[i]))

elif x[0] >= 0:
    ans = x[K - 1]

else:
    ans = abs(x[-K])

print(ans)

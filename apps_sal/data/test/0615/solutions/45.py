N = int(input())
A = list(map(int, input().split()))
S = [0]
for (i, a) in enumerate(A, 1):
    S.append(S[i - 1] + a)
Sn = S[-1]
ans = Sn
i0 = 1
k0 = 3
for j in range(2, N - 1):
    tmpS = S[j]
    for i in range(i0, j):
        if S[i] > tmpS / 2:
            break
    i -= abs(tmpS - S[i] - S[i]) > abs(tmpS - S[i - 1] - S[i - 1])
    i0 = i
    for k in range(k0, N):
        if S[k] - tmpS > (Sn - tmpS) / 2:
            break
    k -= abs(Sn - S[k] - S[k] + tmpS) > abs(Sn - S[k - 1] - S[k - 1] + tmpS)
    k0 = k
    P = (S[i], S[j] - S[i], S[k] - S[j], S[-1] - S[k])
    ans = min(ans, max(P) - min(P))
print(ans)

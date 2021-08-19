(N, K, Q) = list(map(int, input().split()))
A = list(map(int, input().split()))
Ac = [(a, i) for (i, a) in enumerate(A)]
Ac.sort()
ans = Ac[Q - 1][0] - Ac[0][0]
imps = [N]
for j in range(N):
    (a, i) = Ac[j]
    imps.append(i)
    imps.sort()
    kp = 0
    possibles = []
    for k in imps:
        if k - kp >= K:
            Ak = A[kp:k]
            Ak.sort()
            possibles += Ak[:len(Ak) - K + 1]
        kp = k + 1
    if len(possibles) < Q:
        break
    possibles.sort()
    ans = min(ans, possibles[Q - 1] - possibles[0])
print(ans)

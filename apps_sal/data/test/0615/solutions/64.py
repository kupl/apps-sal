N = int(input())
As = list(map(int, input().split()))

ans = float('inf')
iB, iD = 1, 3
(P, Q, R), S = As[:3], sum(As[3:])

# 真ん中の区切りを全通り試す
for iC in range(2, N - 1):
    while P < Q and As[iB] <= Q - P:
        P += As[iB]
        Q -= As[iB]
        iB += 1

    while R < S and As[iD] <= S - R:
        R += As[iD]
        S -= As[iD]
        iD += 1

    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))

    Q += As[iC]
    R -= As[iC]

print(ans)

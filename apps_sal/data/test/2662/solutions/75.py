N = int(input())
A = list(int(input()) for _ in range(N))

S = [A[0]]
for i in range(1, N):
    if A[i] <= S[0]:
        S.insert(0, A[i])
        continue
    ok = 0
    ng = len(S)
    tmp = (ok + ng)
    while ok + 1 < ng:
        tmp = (ok + ng) // 2
        if A[i] > S[tmp]:
            ok = tmp
        else:
            ng = tmp
    S[ok] = A[i]
print((len(S)))

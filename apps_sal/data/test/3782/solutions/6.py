(N, K, Q) = map(int, input().split())
A = list(map(int, input().split()))
ans = 10 ** 18
for Y in set(A):
    L = []
    l = []
    for i in range(N):
        if A[i] < Y:
            L.append(l)
            l = []
        else:
            l.append(A[i])
    L.append(l)
    l2 = []
    for l in L:
        if len(l) <= K - 1:
            continue
        l.sort()
        for i in range(len(l) - K + 1):
            l2.append(l[i])
    if len(l2) < Q:
        continue
    l2.sort()
    X = l2[Q - 1]
    ans = min(ans, X - Y)
print(ans)

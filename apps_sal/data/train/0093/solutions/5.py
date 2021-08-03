T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = [int(a) - 1 for a in input().split()]
    B = [int(a) - 1 for a in input().split()]

    X = [0] * N
    for i, a in enumerate(A):
        X[a] = i
    ans = 0
    ma = -1
    for i, b in enumerate(B):
        ans += (X[b] - i) * 2 + 1 if X[b] > ma else 1
        ma = max(ma, X[b])
    print(ans)

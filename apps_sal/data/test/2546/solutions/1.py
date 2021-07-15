import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, S = list(map(int, input().split()))
    X = []
    for __ in range(N):
        l, r = list(map(int, input().split()))
        X.append((l, r))
        
    ok = 1
    ng = 10**9+1

    while ng - ok > 1:
        m = (ok+ng) // 2

        A = []
        B = []
        for i in range(N):
            if X[i][1] >= m:
                A.append(X[i][0])
            else:
                B.append(X[i][0])

        A = sorted(A)[::-1]
        if len(A) > N//2 and sum([max(a, m) for a in A[:N//2+1]]) + sum(A[N//2+1:]) + sum(B) <= S:
            ok = m
        else:
            ng = m

    print(ok)



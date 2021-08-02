T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    L = N + M - 1
    c0 = [0] * L
    c1 = [0] * L
    for i, row in enumerate(A):
        for j, a in enumerate(row):
            if a == 0:
                c0[i + j] += 1
            else:
                c1[i + j] += 1
    M = L // 2
    ans = 0
    for i in range(M):
        a0 = c0[i] + c0[-1 - i]
        a1 = c1[i] + c1[-1 - i]
        ans += min(a0, a1)
    print(ans)

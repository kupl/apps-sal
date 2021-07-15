Q = int(input())
for _ in range(Q):
    N, K = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    mi = min(A)
    ma = max(A)
    if ma-mi <= 2*K:
        print(mi+K)
    else:
        print(-1)


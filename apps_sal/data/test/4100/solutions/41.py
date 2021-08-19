(N, K, Q) = map(int, input().split())
A = [int(input()) for _ in range(Q)]
p = [K - Q] * N
for i in range(Q):
    p[A[i] - 1] += 1
for i in range(N):
    if p[i] > 0:
        print('Yes')
    else:
        print('No')

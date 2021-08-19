def inpl():
    return list(map(int, input().split()))


(N, K, Q) = inpl()
P = [0] * N
for _ in range(Q):
    a = int(input())
    P[a - 1] += 1
for p in P:
    if K - Q + p > 0:
        print('Yes')
    else:
        print('No')

(N, K, Q) = map(int, input().split())
A = [int(input()) for _ in range(Q)]
L = [K - Q] * N
for a in A:
    L[a - 1] += 1
for l in L:
    print('No' if l < 1 else 'Yes')

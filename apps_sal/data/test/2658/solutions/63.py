N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * (N + 1)
B[0] = 1
if B[0] in A:
    c = B[0]
for i in range(1, N + 1):
    B[i] = A[B[i - 1] - 1]

d = B.index(B[-1]) + 1
if K <= N:
    print((B[K]))
    return
print((B[d - 1 + (K + 1 - d) % (N + 1 - d)]))

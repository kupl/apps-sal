NN = 18
MI = [1 << 100] * ((1 << NN + 1) - 1)


def update(x):
    i = (1 << NN) - 1 + x
    MI[i] = x
    while True:
        i = (i - 1) // 2
        MI[i] = min(MI[2 * i + 1], MI[2 * i + 2])
        if i == 0:
            break


def rangemin(a, b):
    l = a + (1 << NN)
    r = b + (1 << NN)
    mi = 1 << 100
    while l < r:
        if l % 2:
            mi = min(mi, MI[l - 1])
            l += 1
        if r % 2:
            r -= 1
            mi = min(mi, MI[r - 1])
        l >>= 1
        r >>= 1
    return mi


N = int(input())
A = [int(a) for a in input().split()]
B = sorted([(A[i], i) for i in range(N)])
i = 0  # large
j = 0  # small
X = [1 << 20] * (2 * N)
while i < N:
    while 2 * B[j][0] < B[i][0]:
        update(B[j][1])
        update(B[j][1] + N)
        j += 1
    X[B[i][1]] = rangemin(B[i][1], B[i][1] + N)
    X[B[i][1] + N] = X[B[i][1]] + N
    i += 1
for i in range(2 * N - 1)[::-1]:
    X[i] = min(X[i], X[i + 1])
for i in range(N):
    X[i] -= i
X = [a if a < (1 << 20) else -1 for a in X[:N]]
print(*X)

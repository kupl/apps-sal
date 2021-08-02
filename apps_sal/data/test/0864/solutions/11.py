n, m = list(map(int, input().split()))
N = list(map(int, input().split()))
A = [0] * 100
for i in range(m):
    A[N[i] - 1] += 1
X = [0] * 100
f = 0
r = 100000
g = 0
for i in range(n):
    f = 0
    for k in range(100):
        if A[k] // (X[k] + 1) > f:
            f = A[k] // (X[k] + 1)
            g = k
    X[g] += 1
    r = min(r, A[g] // X[g])
print(r)

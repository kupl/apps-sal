n, m, k = map(int, input().split())
x, s = map(int, input().split())
A = [x] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
D = [0] + list(map(int, input().split()))
QW = list(zip(A, B))
QW.sort(key=lambda x: x[1])
A = [s[0] for s in QW]
B = [s[1] for s in QW]

Res = x * n

for i in range(1, k + 1):
    C[i] = max(C[i], C[i - 1])
l = k
e = 10**19

for i in range(m + 1):
    e = min(e, A[i])
    while l >= 0 and B[i] + D[l] > s:
        l -= 1
    if l >= 0:
        Res = min(Res, max(n - C[l], 0) * A[i])


print(Res)

(N, *A) = list(map(int, open(0).read().split()))
v1 = 0
v2 = 0
v3 = 0
m = N // 2 * 2
if N % 2 == 0:
    for i in range(0, m, 2):
        v1 += A[i]
        v2 += A[i + 1]
        v2 = max(v1, v2)
    print(v2)
else:
    for i in range(0, m, 2):
        v1 += A[i]
        v2 += A[i + 1]
        v3 += A[i + 2]
        v2 = max(v1, v2)
        v3 = max(v2, v3)
    print(v3)

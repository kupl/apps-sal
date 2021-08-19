(N, M, C) = map(int, input().split())
B = list(map(int, input().split()))
x = 0
for i in range(N):
    A = list(map(int, input().split()))
    s = C
    for j in range(M):
        s += A[j] * B[j]
    if s > 0:
        x += 1
print(x)

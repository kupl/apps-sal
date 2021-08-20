(N, M) = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * M
d = [0] * M
for i in range(N):
    (a[i], b[i]) = map(int, input().split())
for i in range(M):
    (c[i], d[i]) = map(int, input().split())
for i in range(N):
    min = 0
    for j in range(M):
        if abs(a[i] - c[min]) + abs(b[i] - d[min]) > abs(a[i] - c[j]) + abs(b[i] - d[j]):
            min = j
    print(min + 1)

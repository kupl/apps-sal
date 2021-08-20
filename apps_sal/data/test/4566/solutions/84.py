(N, M) = map(int, input().split())
l = [0] * N
for i in range(M):
    (a, b) = map(int, input().split())
    l[a - 1] += 1
    l[b - 1] += 1
for i in range(N):
    print(l[i])

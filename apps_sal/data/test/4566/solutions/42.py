(N, M) = list(map(int, input().split()))
data = [[] for _ in range(N + 1)]
for i in range(M):
    (x, y) = list(map(int, input().split()))
    data[x].append(y)
    data[y].append(x)
for i in range(1, N + 1):
    print(len(data[i]))

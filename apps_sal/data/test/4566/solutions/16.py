(N, M) = tuple(map(int, input().split()))
count_road = [0 for _ in range(N + 1)]
for _ in range(M):
    (a, b) = tuple(map(int, input().split()))
    count_road[a] += 1
    count_road[b] += 1
for i in range(1, N + 1):
    print(count_road[i])

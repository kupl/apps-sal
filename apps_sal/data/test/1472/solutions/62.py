(N, X, Y) = list(map(int, input().split()))
dist_cnt = [0] * N
for i in range(1, N):
    for j in range(i + 1, N + 1):
        dist = min([j - i, abs(i - X) + abs(j - Y) + 1])
        dist_cnt[dist] += 1
for i in range(1, N):
    print(dist_cnt[i])

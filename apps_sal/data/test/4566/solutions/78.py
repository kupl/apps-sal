(N, M) = map(int, input().split())
cnt = [0 for i in range(N)]
for i in range(M):
    (a, b) = map(int, input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1
for i in range(N):
    print(cnt[i])

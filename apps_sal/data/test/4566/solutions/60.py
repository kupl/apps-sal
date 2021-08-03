n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(m)]
cnt = [0] * n
for i in road:
    cnt[i[0] - 1] += 1
    cnt[i[1] - 1] += 1
for j in range(n):
    print(cnt[j])

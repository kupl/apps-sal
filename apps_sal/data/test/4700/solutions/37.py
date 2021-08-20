(N, M) = map(int, input().split())
H = list(map(int, input().split()))
miti = []
for i in range(M):
    miti.append(list(map(int, input().split())))
count = []
for i in range(N):
    count.append(1)
for i in range(M):
    if H[miti[i][0] - 1] < H[miti[i][1] - 1]:
        count[miti[i][0] - 1] = 0
    if H[miti[i][0] - 1] > H[miti[i][1] - 1]:
        count[miti[i][1] - 1] = 0
    if H[miti[i][0] - 1] == H[miti[i][1] - 1]:
        count[miti[i][0] - 1] = 0
        count[miti[i][1] - 1] = 0
ans = 0
for i in range(N):
    ans += count[i]
print(ans)

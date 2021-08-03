N, M = map(int, input().split())
cnt = [0] * N
history = []
res = [''] * M

for i in range(M):
    P, Y = map(int, input().split())
    history.append((Y, P - 1, i))

history.sort()

for i in range(M):
    cnt[history[i][1]] += 1
    res[history[i][2]] = str(history[i][1] + 1).zfill(6) + str(cnt[history[i][1]]).zfill(6)

for i in range(M):
    print(res[i])

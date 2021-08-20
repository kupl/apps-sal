N = int(input())
Ali = list(map(int, input().split()))
bli = [0] * (N + 1)
M = 0
for z in range(N):
    i = N - z
    sb = 0
    for j in range(i * 2, N + 1, i):
        sb += bli[j]
    if sb % 2 != Ali[i - 1]:
        bli[i] = 1
        M += 1
print(M)
cnt = 0
for i in range(N + 1):
    if bli[i] == 1:
        cnt += 1
        if cnt == M:
            print(i)
        else:
            print(i, end=' ')

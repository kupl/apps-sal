N = int(input())
V = [int(input()) for i in range(1, N + 1)]
cnt = 1
val = V[0]
while True:
    if val == 2:
        print(cnt)
        break
    if (cnt >= N):
        print((-1))
        break
    cnt += 1
    val = V[val - 1]

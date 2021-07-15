N = int(input())
L = []
light = [0]*(N)
light[0] = 1
cnt, now = 0, 0

for i in range(N):
    L.append(int(input()))

for i in range(N):
    now = L[now] - 1
    cnt += 1
    if now == 1:
        print(cnt)
        return

print((-1))


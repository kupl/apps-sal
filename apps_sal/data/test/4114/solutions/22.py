N = int(input())
p = [0] * N
for i in range(N):
    p[i] = list(map(int, input().split()))

for i in range(N):
    if p[i][2] > 0:
        pp = p[i]

f = 0

for i in range(101):
    for j in range(101):
        H = pp[2] + abs(i - pp[0]) + abs(j - pp[1])
        for k in range(N):
            if p[k][2] != max(H - abs(i - p[k][0]) - abs(j - p[k][1]), 0):
                break
            if k == (N - 1):
                xa = i
                ya = j
                Ha = H
                f = 1
                break
        if f == 1:
            break
    if f == 1:
        break


print(xa, ya, Ha)

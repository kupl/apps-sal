N = int(input())
AB = [0] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))
AB = sorted(AB)
CD = [0] * N
for i in range(N):
    CD[i] = list(map(int, input().split()))
CD = sorted(CD)
ans = 0
used = [0] * N
for i in range(N):
    (now_x, now_y) = (CD[i][0], CD[i][1])
    max_y = -1
    nn = -1
    for j in range(N):
        if now_x > AB[j][0] and used[j] == 0:
            if now_y > AB[j][1]:
                if max_y < AB[j][1]:
                    max_y = AB[j][1]
                    nn = j
    if max_y != -1:
        ans += 1
        used[nn] = 1
print(ans)

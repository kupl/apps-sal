N = int(input())
txy = [[0, 0, 0]]
for i in range(N):
    txy.append(list(map(int, input().split())))
for i in range(N):
    dt = txy[i + 1][0] - txy[i][0]
    dx = txy[i + 1][1] - txy[i][1]
    dy = txy[i + 1][2] - txy[i][2]
    if dt < abs(dx + dy):
        print('No')
        break
    elif (dt - (dx + dy)) % 2 != 0:
        print('No')
        break
else:
    print('Yes')

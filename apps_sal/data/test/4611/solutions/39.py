n = int(input())

txy = [list(map(int, input().split())) for _ in range(n)]
txy = [[0, 0, 0]] + txy

for i in range(n):
    move = abs(txy[i + 1][1] - txy[i][1]) + abs(txy[i + 1][2] - txy[i][2])
    time = txy[i + 1][0] - txy[i][0]
    if time % 2 ^ move % 2 == 1 or time < move:
        print("No")
        return

print("Yes")

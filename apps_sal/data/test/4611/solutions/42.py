N = int(input())

Input = []
for i in range(N):
    Input.append(list(map(int, input().split())))

position = {"x":0, "y":0}
preT = 0
for i in range(N):
    T = Input[i][0]
    x = Input[i][1]
    y = Input[i][2]

    move = abs(position["x"] - x) + abs(position["y"] - y)
    if move > (T - preT) or move % 2 != (T - preT) % 2:
        print("No")
        return

    preT = T
    position["x"] = x
    position["y"] = y

print("Yes")

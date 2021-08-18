H, W = map(lambda x: int(x) + 2, input().split())
grid = "." * W
for _ in range(H - 2):
    grid += "." + input() + "."
grid += "." * W

Flag = True
move_list = [1, -1, W, -W]

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if grid[i * W + j] == "
        Flag = False
        break

if Flag:
    print("Yes")
else:
    print("No")

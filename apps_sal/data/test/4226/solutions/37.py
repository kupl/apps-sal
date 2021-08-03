x, y = list(map(int, input().split()))
flag = True
for animal in range(1, x + 1):
    if y == animal * 4 + (x - animal) * 2 or y == animal * 2 + (x - animal) * 4:
        print("Yes")
        flag = False
        break
if flag:
    print("No")

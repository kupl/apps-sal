w, b = list(map(int, input().split()))
grid = []
for i in range(50):
    grid.append(["."] * 100)
for i in range(50):
    grid.append(["
w -= 1
b -= 1
cnt=0
i=0
j=0
while cnt < b:
    grid[i][j]= "
    if j == 98:
        i += 2
        j=1
    elif j == 99:
        i += 2
        j=0
    else:
        j += 2
    cnt += 1

cnt=0
i=51
j=0
while cnt < w:
    grid[i][j]="."
    if j == 98:
        i += 2
        j=1
    elif j == 99:
        i += 2
        j=0
    else:
        j += 2
    cnt += 1
print((100, 100))
for i in range(len(grid)):
    print(("".join(grid[i])))

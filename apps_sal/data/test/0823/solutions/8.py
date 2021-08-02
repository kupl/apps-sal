
s = input().split()
x = (int(s[0]))
y = (int(s[1]))

dirx = [1, 0, -1, 0]
diry = [0, 1, 0, -1]

if x == 0 and y == 0:
    print(0)
else:
    cx = 0
    cy = 0
    dir = 0
    steps = 1
    count = 0
    done = False
    while not done:
        for i in range(steps):
            cx += dirx[dir]
            cy += diry[dir]
            if cx == x and cy == y:
                print(count)
                done = True
                break
        count += 1
        dir = (dir + 1) % 4
        if dir == 0 or dir == 2:
            steps += 1

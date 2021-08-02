def solv():
    x, y = map(int, input().split())
    grid = [input() for n in range(x)]
    res = 0
    for n in range(x - 1):
        if grid[n][-1] == 'R':
            res += 1
    for n in range(y - 1):
        if grid[-1][n] != 'R': res += 1

    print(res)


for _ in range(int(input())):
    solv()

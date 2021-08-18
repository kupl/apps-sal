import sys


mem = []
for i in range(32):
    mem.append([[-1] * 52 for u in range(32)])


def solve(x, y, z):
    if x > y:
        mem[x][y][z] = solve(y, x, z)
        return mem[x][y][z]
    if x * y == z or z == 0:
        mem[x][y][z] = 0
        return 0
    if x * y < z:
        mem[x][y][z] = -2
        return -2
    res = -2
    for i in range(1, x // 2 + 1):
        for eaten in range(z + 1):
            t1 = mem[i][y][eaten] if mem[i][y][eaten] != -1 else solve(i, y, eaten)
            if t1 == -2:
                continue
            t2 = mem[x - i][y][z - eaten] if mem[x - i][y][z - eaten] != -1 else solve(x - i, y, z - eaten)
            if t2 == -2:
                continue
            if res == -2 or res > t1 + t2 + y * y:
                res = t1 + t2 + y * y

    for j in range(1, y // 2 + 1):
        for eaten in range(z + 1):
            t1 = mem[x][j][eaten] if mem[x][j][eaten] != -1 else solve(x, j, eaten)
            if t1 == -2:
                continue
            t2 = mem[x][y - j][z - eaten] if mem[x][y - j][z - eaten] != -1 else solve(x, y - j, z - eaten)
            if t2 == -2:
                continue
            if res == -2 or res > t1 + t2 + x * x:
                res = t1 + t2 + x * x

    mem[x][y][z] = res
    return mem[x][y][z]


t = int(sys.stdin.readline())
for it in range(t):
    n, m, k = list(map(int, sys.stdin.readline().split()))
    print(solve(n, m, k))

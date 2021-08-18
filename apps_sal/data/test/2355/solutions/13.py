t = int(input())


def readints():
    return map(int, input().split(' '))


def solve():
    n, p = readints()
    viz = [[0] * n for _ in range(n)]
    for j in range(n):
        viz[0][j] = viz[j][0] = 1
    for j in range(n):
        viz[1][j] = viz[j][1] = 1
    leftover = p + 3
    done = False
    for i in range(n):
        if done:
            break
        for j in range(i + 1, n):
            if viz[i][j] == 1:
                continue
            leftover -= 1
            viz[i][j] = viz[j][i] = 1
            if leftover == 0:
                done = True
                break
    for i in range(n):
        for j in range(i + 1, n):
            if viz[i][j]:
                print(i + 1, j + 1)


for _ in range(t):
    solve()

import sys


def __starting_point():
    bingo = [[0] * 3 for i in range(3)]
    ans = [[0] * 3 for i in range(3)]
    for i in range(3):
        temp = list(map(int, input().split()))
        for j in range(3):
            bingo[i][j] = temp[j]
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if bingo[j][k] == b:
                    ans[j][k] = 1
    for i in range(3):
        if ans[0][i] + ans[1][i] + ans[2][i] == 3:
            print('Yes')
            return
    for i in range(3):
        if ans[i][0] + ans[i][1] + ans[i][2] == 3:
            print('Yes')
            return
    if ans[0][0] + ans[1][1] + ans[2][2] == 3:
        print('Yes')
        return
    if ans[0][2] + ans[1][1] + ans[2][0] == 3:
        print('Yes')
        return
    print('No')


__starting_point()

from sys import stdin

n = int(stdin.readline())
nn = [[int(x) for x in stdin.readline().rstrip()] for i in range(n)]


def run():
    for row in range(n):
        for col in range(n):
            if(nn[row][col] == 0):
                continue
            if(countAdj(row, col, n - 1)):
                print('No')
                return 0
    print('Yes')


def countAdj(row, col, n):
    cnt = 0
    adj = 0
    if(row > 1 and nn[row - 1][col]):
        cnt += 1
        adj += nn[row - 1][col]
    if(row < n and nn[row + 1][col]):
        cnt += 1
        adj += nn[row + 1][col]
    if(col > 1 and nn[row][col - 1]):
        cnt += 1
        adj += nn[row][col - 1]
    if(col < n and nn[row][col + 1]):
        cnt += 1
        adj += nn[row][col + 1]

    if(cnt <= 1):
        return True
    elif(cnt < 4 and nn[row][col] == cnt - 1):
        if(nn[row][col] == 1 and adj != 4):
            return True
        if(nn[row][col] == 2 and not (6 <= adj <= 8)):
            return True
        return False
    elif(cnt == 4 and nn[row][col] == cnt):
        if(nn[row][col] == 4 and not (adj == 8 or adj == 10 or adj == 12 or adj == 14 or adj == 16)):
            return True
        return False
    return True


run()

def pos(x, num):
    if x < 0:
        return -1
    elif x >= num:
        return -1
    return x


def check(x, y, ai, n, m):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if pos(x + i, n) == -1 or pos(y + j, m) == -1:
                continue
            if ai[pos(x + i, n)][pos(y + j, m)] == "*":
                num += 1
    return num


n, m = list(map(int, input().split()))
ai = [input() for i in range(n)]
ans = 1
for i in range(n):
    for j in range(m):
        if ai[i][j] == "*":
            continue
        temp = 0
        if ai[i][j] != ".":
            temp = int(ai[i][j])
        if temp != check(i, j, ai, n, m):
            ans = 0
if ans == 0:
    print("NO")
else:
    print("YES")

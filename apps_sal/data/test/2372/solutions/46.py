H, W = list(map(int, input().split()))
Ch, Cw = list(map(int, input().split()))
Dh, Dw = list(map(int, input().split()))

Ch += 1
Cw += 1
Dh += 1
Dw += 1

start = (Ch, Cw)

S = ['#' * (W + 4)]
S.append('#' * (W + 4))
for k in range(H):
    S.append('##' + input() + '##')
S.append('#' * (W + 4))
S.append('#' * (W + 4))

counter = [[-1 for _ in range(W + 4)] for _ in range(H + 4)]
for k in range(2, H + 2):
    for j in range(2, W + 2):
        if S[k][j] == '.':
            counter[k][j] = 10**7

counter[Ch][Cw] = 0

# print(counter)
# print(S)

now = [start]
now_2 = [start]
while len(now_2) > 0:
    new = []
    for item in now_2:
        x = item[0]
        y = item[1]
        if counter[x + 1][y] == 10**7:
            counter[x + 1][y] = 0
            new.append((x + 1, y))
        if counter[x][y + 1] == 10**7:
            counter[x][y + 1] = 0
            new.append((x, y + 1))
        if counter[x - 1][y] == 10**7:
            counter[x - 1][y] = 0
            new.append((x - 1, y))
        if counter[x][y - 1] == 10**7:
            counter[x][y - 1] = 0
            new.append((x, y - 1))
    now += new
    now_2 = new
# print(now)
# print(counter)
if counter[Dh][Dw] == 0:
    print((0))
    return
ans = 0
while counter[Dh][Dw] == 10**7:
    if len(now) == 0:
        print((-1))
        return
    nextlist = []
    ans += 1
    for item in now:
        x = item[0]
        y = item[1]
        if counter[x + 2][y + 2] > ans:
            counter[x + 2][y + 2] = ans
            nextlist.append((x + 2, y + 2))
        if counter[x + 2][y + 1] > ans:
            counter[x + 2][y + 1] = ans
            nextlist.append((x + 2, y + 1))
        if counter[x + 2][y] > ans:
            counter[x + 2][y] = ans
            nextlist.append((x + 2, y))
        if counter[x + 2][y - 1] > ans:
            counter[x + 2][y - 1] = ans
            nextlist.append((x + 2, y - 1))
        if counter[x + 2][y - 2] > ans:
            counter[x + 2][y - 2] = ans
            nextlist.append((x + 2, y - 2))
        if counter[x + 1][y + 2] > ans:
            counter[x + 1][y + 2] = ans
            nextlist.append((x + 1, y + 2))
        if counter[x + 1][y - 2] > ans:
            counter[x + 1][y - 2] = ans
            nextlist.append((x + 1, y - 2))
        if counter[x][y + 2] > ans:
            counter[x][y + 2] = ans
            nextlist.append((x, y + 2))
        if counter[x][y - 2] > ans:
            counter[x][y - 2] = ans
            nextlist.append((x, y - 2))
        if counter[x - 2][y + 2] > ans:
            counter[x - 2][y + 2] = ans
            nextlist.append((x - 2, y + 2))
        if counter[x - 2][y + 1] > ans:
            counter[x - 2][y + 1] = ans
            nextlist.append((x - 2, y + 1))
        if counter[x - 2][y] > ans:
            counter[x - 2][y] = ans
            nextlist.append((x - 2, y))
        if counter[x - 2][y - 1] > ans:
            counter[x - 2][y - 1] = ans
            nextlist.append((x - 2, y - 1))
        if counter[x - 2][y - 2] > ans:
            counter[x - 2][y - 2] = ans
            nextlist.append((x - 2, y - 2))
        if counter[x - 1][y + 2] > ans:
            counter[x - 1][y + 2] = ans
            nextlist.append((x - 1, y + 2))
        if counter[x - 1][y - 2] > ans:
            counter[x - 1][y - 2] = ans
            nextlist.append((x - 1, y - 2))
        if counter[x - 1][y - 1] > ans:
            counter[x - 1][y - 1] = ans
            nextlist.append((x - 1, y - 1))
        if counter[x - 1][y + 1] > ans:
            counter[x - 1][y + 1] = ans
            nextlist.append((x - 1, y + 1))
        if counter[x + 1][y + 1] > ans:
            counter[x + 1][y + 1] = ans
            nextlist.append((x + 1, y + 1))
        if counter[x + 1][y - 1] > ans:
            counter[x + 1][y - 1] = ans
            nextlist.append((x + 1, y - 1))

    now_2 = nextlist
    while len(now_2) > 0:
        new = []
        for item in now_2:
            x = item[0]
            y = item[1]
            if counter[x + 1][y] == 10**7:
                counter[x + 1][y] = 0
                new.append((x + 1, y))
            if counter[x][y + 1] == 10**7:
                counter[x][y + 1] = 0
                new.append((x, y + 1))
            if counter[x - 1][y] == 10**7:
                counter[x - 1][y] = 0
                new.append((x - 1, y))
            if counter[x][y - 1] == 10**7:
                counter[x][y - 1] = 0
                new.append((x, y - 1))
        nextlist += new
        now_2 = new
    now = nextlist
    # print(now)
    if ans > 10**7:
        print((-1))
        return
print(ans)

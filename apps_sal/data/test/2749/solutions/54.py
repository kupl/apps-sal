h, w = map(int, input().split())
n = int(input())
colors = list(map(int, input().split()))
cmap = [(i + 1, a) for i, a in enumerate(colors)]
campus = [0] * (h * w)


def printmtrx(campus):
    ts = ""
    for idx, i in enumerate(campus):
        if((idx + 1) % w == 1):
            if idx == 0:
                ts += str(i) + " "
            else:
                ts += "\n" + str(i) + " "
        else:
            if (idx + 1) % w == 0:
                ts += str(i)
            else:
                ts += str(i) + " "
    print(ts)


def printmtrx2(campus):
    cnt = 0
    for i in range(h):
        ts = ""
        for j in range(w):
            if not j == 0:
                ts += " "
            ts += str(campus[cnt])
            cnt += 1
        print(ts)

# print(cmap)
# print(campus)


cnt = cmap[0][1]
idx = 0
campusidx = 0
direct = 0
while cnt:
    # print(campusidx)
    # printmtrx(campus)
    # print("")
    campus[campusidx] = cmap[idx][0]
    cnt -= 1
    if(cnt < 1):
        idx += 1
        if(idx >= len(cmap)):
            break
        cnt = cmap[idx][1]
    campusidx += 1 - 2 * direct
    if campusidx % w == 0 and direct == 0:
        campusidx += w - 1
        direct = 1
    elif campusidx % w == w - 1 and direct == 1:
        campusidx += w + 1
        direct = 0
printmtrx2(campus)

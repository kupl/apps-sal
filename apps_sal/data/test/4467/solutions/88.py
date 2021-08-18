import sys


def resolve():
    readline = sys.stdin.readline

    N = int(readline())
    NN = 2 * N + 1

    red = [[] for _ in [0] * NN]
    blue = [[] for _ in [0] * NN]
    for _ in [0] * N:
        a, b = list(map(int, readline().split()))
        red[b].append(a)
    for _ in [0] * N:
        c, d = list(map(int, readline().split()))
        blue[c].append(d)

    for i in range(NN):
        r = red[i]
        b = blue[i]
        r.sort(reverse=True)
        b.sort(reverse=True)
        r[0:0] = [i]
        b[0:0] = [i]

    ans = 0
    flag = False
    while blue:
        cd_blue = blue.pop(0)
        c = cd_blue.pop(0)
        if cd_blue:
            for d in cd_blue:
                for ba_red in red[::-1]:
                    b = ba_red[0]
                    if ba_red[1:]:
                        for i in range(1, len(ba_red)):
                            a = ba_red[i]
                            if a <= c and b <= d:
                                ans += 1
                                del red[b][i]
                                flag = True
                                break
                        if flag:
                            break
                if flag:
                    flag = False
                    break
    print(ans)


resolve()

import sys


def resolve():
    readline = sys.stdin.readline    # 1行だけ文字列にする

    N = int(readline())
    NN = 2 * N + 1

    # 青色はx座標をlistのindex,y座標をlistのvalueとして入力，赤は逆
    red = [[] for _ in [0] * NN]
    blue = [[] for _ in [0] * NN]
    for _ in [0] * N:
        a, b = list(map(int, readline().split()))
        red[b].append(a)
    for _ in [0] * N:
        c, d = list(map(int, readline().split()))
        blue[c].append(d)

    # 青色でvalueのy座標について降順(大きい順)でソート
    # 赤色ではvalueのx座標について降順でソート
    # これで青色はx座標は昇順(index)，y座標は降順(value)にソートされる
    # 赤色はy座標が昇順(index)，x座標が降順(value)
    for i in range(NN):
        r = red[i]
        b = blue[i]
        r.sort(reverse=True)
        b.sort(reverse=True)
        r[0:0] = [i]
        b[0:0] = [i]

    # 青点はx座標の昇順で，赤点はy座標の降順
    # 最小のxの青点で最大のyを持つ赤点を選択
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

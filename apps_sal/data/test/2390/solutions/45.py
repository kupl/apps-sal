import sys

input = sys.stdin.readline


def main():
    N, C = [int(x) for x in input().split()]
    XV = [[int(x) for x in input().split()] for _ in range(N)]

    migi = [0]
    last = 0
    for x, v in XV:
        migi.append(migi[-1] + v - x + last)
        last = x

    hidari = [0]
    last = C
    for x, v in XV[::-1]:
        hidari.append(hidari[-1] + v - (last - x))
        last = x

    ans = max(max(migi), max(hidari))

    migimax = []
    ma = 0
    for m in migi:
        ma = max(ma, m)
        migimax.append(ma)

    hidarimax = []
    ma = 0
    for m in hidari:
        ma = max(ma, m)
        hidarimax.append(ma)

    for i in range(N):
        ans = max(ans, migi[i + 1] - XV[i][0] + hidarimax[N - i - 1])

    for i in range(N):
        ans = max(ans, hidari[i + 1] - (C - XV[-i - 1][0]) + migimax[N - i - 1])

    print(ans)


def __starting_point():
    main()

__starting_point()

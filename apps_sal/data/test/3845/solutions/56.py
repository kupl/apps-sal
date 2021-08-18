import sys
input = sys.stdin.buffer.readline


def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def TI(): return tuple(map(int, input().split()))


def main():
    a, b = MI()

    G = []

    for _ in range(25):
        G += [list("...


    for i in range(25):
        for j in range(24):
            if a < 25**2:
                G[4 * i][4 * j + 3]="."
                a += 1
            else:
                break

    for i in range(25):
        if a < 25**2:
            G[4 * i + 3][0]="."
            a += 1
        else:
            break

    for i in range(25):
        for j in range(25):
            if b < 25**2 + 1:
                G[4 * i + 1][4 * j + 1]="."
                b += 1

    print(100, 100)

    for i in G:
        print(*i, sep="")


def __starting_point():
    main()


__starting_point()

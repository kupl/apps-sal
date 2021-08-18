import sys
input = sys.stdin.buffer.readline


def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return list(map(int, input().split()))
def MF(): return list(map(float, input().split()))
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def TI(): return tuple(map(int, input().split()))


def main():
    k = II()

    q, r = divmod(k, 50)

    N = [49 + q + 50 - r + 1] * r + [49 + q - r] * (50 - r)
    print((50))
    print((*N))


def __starting_point():
    main()


__starting_point()

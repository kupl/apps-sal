import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readlines


def main():
    lines = input()

    n, l = list(map(int, lines[0].split()))

    Sum_ = int(n * (l - 1) + n * (n + 1) / 2)

    if l >= 0:
        print(Sum_ - l)
        return
    else:
        if n + l - 1 <= 0:
            print(Sum_ - (l + n - 1))
        else:
            print(Sum_)


main()

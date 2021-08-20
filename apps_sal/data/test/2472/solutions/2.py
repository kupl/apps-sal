import sys
input = sys.stdin.readline


def main():
    N = int(input())
    T = [list(map(int, input().split())) for i in range(N)]
    S = [[b, a] for (a, b) in T]
    U = sorted(S)
    time = 0
    for (b, a) in U:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()

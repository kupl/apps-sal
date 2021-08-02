import sys
input = sys.stdin.readline


def main():
    X, Y, A, B, C = map(int, input().split())
    P = sorted(list(map(int, input().split())))
    Q = sorted(list(map(int, input().split())))
    R = sorted(list(map(int, input().split())))

    l = sorted(P[-X:] + Q[-Y:])
    ans = 0
    for i in range(len(l)):
        if len(R) > 0 and R[-1] > l[i]:
            ans += R.pop(-1)
        else:
            ans += l[i]
    print(ans)


def __starting_point():
    main()


__starting_point()

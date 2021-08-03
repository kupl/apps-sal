import sys


def main():
    n, a, b = list(map(int, sys.stdin.readline().split()))
    x = list(map(int, sys.stdin.readline().split()))
    c = 0
    ans = 0
    for i in range(n):
        t = x[i]
        if t == 1:
            if a != 0:
                a -= 1
            elif b != 0:
                b -= 1
                c += 1
            elif c != 0:
                c -= 1
            else:
                ans += 1
        else:
            if b != 0:
                b -= 1
            else:
                ans += 2

    print(ans)


main()

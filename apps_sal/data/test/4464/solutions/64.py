from sys import stdin, stdout


def solve():
    a, b, c = list(map(int, input().split()))
    possible = False
    for k in range(b):
        if (a * k - c) % b == 0:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")


def main():
    solve()


def __starting_point():
    main()


__starting_point()

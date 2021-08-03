import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    L = 0
    R = 0
    for s in S:
        if s == "(":
            R += 1
        else:
            if R > 0:
                R -= 1
            else:
                L += 1

    ans = "".join(["(" * L, S, ")" * R])
    print(ans)


def __starting_point():
    main()


__starting_point()

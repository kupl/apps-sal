import sys
input = sys.stdin.readline


def main():
    S = input().rstrip()
    k = int(input())

    for i in range(k):
        if S[i] != "1":
            break
    print(S[i])


def __starting_point():
    main()


__starting_point()

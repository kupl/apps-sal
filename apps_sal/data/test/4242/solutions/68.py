import sys
input = sys.stdin.readline


def main():
    A, B, K = [int(x) for x in input().split()]

    yakusu = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            yakusu.append(i)

    print((sorted(yakusu, reverse=True)[K - 1]))



def __starting_point():
    main()


__starting_point()

import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for i in range(t):
        a, b, k = list(map(int, input().split()))
        if k % 2 == 0:
            answer = a * (k // 2) - b * (k // 2)
        else:
            answer = a * ((k // 2) + 1) - b * (k // 2)
        print(answer)
    return


def __starting_point():
    main()


__starting_point()

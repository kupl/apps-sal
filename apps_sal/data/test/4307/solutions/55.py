import sys
input = sys.stdin.readline


def slove():
    N = int(input())
    answer = 0
    for x in range(1, N + 1, 2):
        count = 0
        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
        if count == 8:
            answer += 1
    print(answer)


def __starting_point():
    slove()


__starting_point()

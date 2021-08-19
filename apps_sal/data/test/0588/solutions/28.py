import math


def main():
    N = int(input())
    E = []
    for i in range(N):
        (x, y) = list(map(int, input().split()))
        E.append((math.atan2(y, x), x, y))
    E = sorted(E) * 2
    answer = 0
    for i in range(N):
        x = 0
        y = 0
        for j in range(i, i + N):
            x += E[j][1]
            y += E[j][2]
            answer = max(answer, x * x + y * y)
    answer = math.sqrt(answer)
    print(answer)


def __starting_point():
    main()


__starting_point()

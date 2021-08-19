CIRCLE = 1
RECTANGLE = 2
SQUARE = 3


def main():
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0
    for i in range(1, n):
        if a[i - 1] == CIRCLE:
            if a[i] == RECTANGLE:
                answer += 3
                if i > 1 and a[i - 2] == SQUARE:
                    answer -= 1
            else:
                answer += 4
        elif a[i - 1] == RECTANGLE:
            if a[i] == CIRCLE:
                answer += 3
            else:
                print('Infinite')
                return
        elif a[i - 1] == SQUARE:
            if a[i] == CIRCLE:
                answer += 4
            else:
                print('Infinite')
                return
    print('Finite')
    print(answer)


def __starting_point():
    main()


__starting_point()

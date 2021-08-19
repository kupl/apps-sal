def main():
    import sys
    input = sys.stdin.readline
    (x, y) = map(int, input().split())
    answer = 0
    if x == 1:
        answer = 1
        while pow(2, answer) <= y:
            answer += 1
    else:
        while x * pow(2, answer) <= y:
            answer += 1
    print(answer)


def __starting_point():
    main()


__starting_point()

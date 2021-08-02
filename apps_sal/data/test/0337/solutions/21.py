import sys
#input = sys.stdin.readline


def main():
    w, h = map(int, input().split())
    u1, d1 = map(int, input().split())
    u2, d2 = map(int, input().split())
    answer = w
    while h != 0:
        if h == d1:
            answer += h - u1
        elif h == d2:
            answer += h - u2
        else:
            answer += h
        h -= 1
        if answer < 0:
            answer = 0
    print(answer)


def __starting_point():
    main()


__starting_point()

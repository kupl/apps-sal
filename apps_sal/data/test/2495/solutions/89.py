def main():
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    cur, cnt_1 = 0, 0
    for i, j in enumerate(lst):
        new = cur + j
        if i % 2 == 0 and new <= 0:
            cnt_1 += abs(new) + 1
            cur = 1
        elif i % 2 == 1 and new >= 0:
            cnt_1 += abs(new) + 1
            cur = -1
        else:
            cur = new

    cur, cnt_2 = 0, 0
    for i, j in enumerate(lst):
        new = cur + j
        if i % 2 == 0 and new >= 0:
            cnt_2 += abs(new) + 1
            cur = -1
        elif i % 2 == 1 and new <= 0:
            cnt_2 += abs(new) + 1
            cur = 1
        else:
            cur = new
    print(min(cnt_1, cnt_2))


def __starting_point():
    main()


__starting_point()

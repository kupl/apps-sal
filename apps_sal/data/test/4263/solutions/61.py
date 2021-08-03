
target_a = ['A', 'C', 'G', 'T']


def main():
    S = str(input())

    max_cnt = 0
    cnt = 0
    for s in S:
        if s in target_a:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    print(max_cnt)


def __starting_point():
    main()


__starting_point()

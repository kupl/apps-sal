def main():
    n, s = input().split()

    ans = 0

    # 文字列のスタート位置
    for i in range(int(n)):
        at_cnt = 0
        gc_cnt = 0
        for si in s[i:int(n)]:
            if si == 'A':
                at_cnt += 1
            elif si == 'T':
                at_cnt -= 1
            elif si == 'C':
                gc_cnt += 1
            elif si == 'G':
                gc_cnt -= 1

            if at_cnt == 0 and gc_cnt == 0:
                ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()

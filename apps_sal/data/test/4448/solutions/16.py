from collections import deque


def main():
    n, m = list(map(int, input().split()))
    wanted_cnt = list(map(int, input().split()))
    Order = [tuple(map(int, input().split())) for i in range(m)]
    #count the maximum number which you can buy on sales day.
    S = sum(wanted_cnt)

    def ispossible_within(Day):
        sale_get_cnt = 0
        last_sale = [0]*n
        for day, good in Order:
            if day > Day:
                continue
            last_sale[good-1] = max(last_sale[good-1], day)
        Que = []
        for i in range(n):
            if wanted_cnt[i] > 0 and last_sale[i] > 0:
                Que.append((last_sale[i], wanted_cnt[i]))
        Que.sort()
        que = deque(Que)
        while que:
            sale_day, wanted = que.popleft()
            money_left = sale_day - sale_get_cnt
            if money_left >= wanted:
                sale_get_cnt += wanted
            elif money_left < wanted:
                sale_get_cnt += money_left
        left_money = Day - sale_get_cnt
        left = S - sale_get_cnt

        return left_money >= 2*left

    impossible = 0
    possible = 2020
    while possible - impossible > 1:
        m = (impossible + possible)//2
        if ispossible_within(m):
            possible = m
        else:
            impossible = m
    print(possible)
    return


def __starting_point():
    main()


__starting_point()

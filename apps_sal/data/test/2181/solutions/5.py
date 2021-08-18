
import sys


def main():
    a, d = [int(round(float(x) * 10000)) for x in input().split(' ')]
    ans = []

    for i in range(1, int(input()) + 1):
        cur_round_pos = d * i % (a * 4)
        if cur_round_pos <= a:
            y = 0
            x = cur_round_pos / 10000
        elif cur_round_pos <= a * 2:
            x = a / 10000
            y = (cur_round_pos - a) / 10000
        elif cur_round_pos <= a * 3:
            y = a / 10000
            x = (a * 3 - cur_round_pos) / 10000
        elif cur_round_pos < a * 4:
            x = 0
            y = (a * 4 - cur_round_pos) / 10000
        ans.append('{} {}'.format(x, y))

    print('\n'.join(ans))


def __starting_point():
    return(main())


__starting_point()

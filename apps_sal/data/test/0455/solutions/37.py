
def get_check(num, place):
    dist = abs(place[0][0]) + abs(place[0][1])
    check_flg = dist

    for i in range(num - 1):
        dist_now = abs(place[i + 1][0]) + abs(place[i + 1][1])
        if dist % 2 != dist_now % 2:
            check_flg = 0
            break
        if check_flg < dist_now:
            check_flg = dist_now
    return check_flg


def start_process(num, place):

    check_flg = get_check(num, place)
    if check_flg:

        seeds = [2 ** (31 - i) for i in range(32)]
        if check_flg % 2 == 0:
            seeds.append(1)
        print(len(seeds))
        print(' '.join(map(str, seeds)))

        for x, y in place:
            for k in seeds:
                if abs(x) > abs(y):
                    if x > 0:
                        res = 'R'
                        x -= k
                    else:
                        res = 'L'
                        x += k
                else:
                    if y > 0:
                        res = 'U'
                        y -= k
                    else:
                        res = 'D'
                        y += k
                print(res, end='')
            print('')

    else:
        print(-1)


def main():
    num = int(input())
    place = [list(map(int, input().split())) for i in range(num)]
    start_process(num, place)


def __starting_point():
    main()


__starting_point()

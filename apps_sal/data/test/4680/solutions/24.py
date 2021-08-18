
def __starting_point():
    str_list = list(map(int, input().split()))
    if sum(str_list) == 17:
        print('YES')
    else:
        print('NO')


__starting_point()

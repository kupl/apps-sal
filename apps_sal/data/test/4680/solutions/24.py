# -*- coding: utf-8 -*-

def __starting_point():
    # str_list = [map(int, input().split())]
    # if str_list.count(5) == 2 and str_list.count(7) == 1:
    #     print('YES')
    # else:
    #     print('NO')
    str_list = list(map(int, input().split()))
    if sum(str_list) == 17:
        print('YES')
    else:
        print('NO')


__starting_point()

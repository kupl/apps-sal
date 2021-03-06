"""
Created on 27-Feb-2016

@author: venkatesh
"""


def is_row_wise(a, n, k):
    for i in range(n):
        flag = True
        cnt = 0
        for j in range(n):
            if a[i][j] == 'X':
                cnt += 1
            if a[i][j] == '.' and flag:
                cnt += 1
                flag = False
            if cnt == k:
                return True
    return False


def is_column_wise(a, n, k):
    for i in range(n):
        flag = True
        cnt = 0
        for j in range(n):
            if a[j][i] == 'X':
                cnt += 1
            if a[j][i] == '.' and flag:
                cnt += 1
                flag = False
            if cnt == k:
                return True
    return False


def is_diag_wise(a, n, k):
    (cnt, flag) = (0, True)
    for i in range(n):
        if a[i][i] == 'X':
            cnt += 1
        if a[i][i] == '.' and flag:
            cnt += 1
            flag = False
        if cnt == k:
            return True
    (cnt, flag) = (0, True)
    for i in range(n):
        if a[i][n - 1 - i] == 'X':
            cnt += 1
        if a[i][n - 1 - i] == '.' and flag:
            cnt += 1
            flag = False
        if cnt == k:
            return True
    return False


def read_int():
    return int(input())


def read_int_list():
    return [int(x) for x in input().split()]


def is_chef_wins(game, n, k):
    if is_row_wise(game, n, k):
        return True
    elif is_column_wise(game, n, k):
        return True
    elif is_diag_wise(game, n, k):
        return True
    else:
        return False


def main():
    tc = read_int()
    for _ in range(tc):
        (n, k) = read_int_list()
        game = [input() for _ in range(n)]
        print('YES' if is_chef_wins(game, n, k) else 'NO')


def __starting_point():
    main()


__starting_point()

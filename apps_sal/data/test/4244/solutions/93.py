# coding=utf-8

# lib
#import copy
#import collections
#import sys
'''
def generate_2d_array(Row, Column, IV):
    array = [[IV] * Column for i in range(Row)]
    return array


def search_in_2d_array(array, Row, Column, V):
    cnt = 0
    for i in range(Column):
        for j in range(Row):
            if array[i][j] == V:
                cnt += 1
    return cnt


def input_2d_array(Row, Column):
    array = generate_2d_array(Row, Column, 0)

    for i in range(Column):
        temp = list(map(int, input().split()))
        for j in range(Row):
            array[i][j] = temp[j]

    return array
'''


def __starting_point():
    N = int(input())
    Xli = list(map(int, input().split()))

    ans = float('inf')

    for i in range(101):
        cnt = 0

        for j in range(N):
            cnt += abs(Xli[j] - i)**2

        ans = min(ans, cnt)

    print(ans)


__starting_point()

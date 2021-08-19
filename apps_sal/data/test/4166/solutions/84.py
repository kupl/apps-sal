# coding=utf-8

# lib
#import copy
#import collections
import sys


def generate_2d_array(Row, Column, IV):
    array = [[IV] * Row for i in range(Column)]
    return array


'''
def search_in_2d_array(array, Row, Column, V):
    cnt = 0
    for i in range(Column):
        for j in range(Row):
            if array[i][j] == V:
                cnt += 1
    return cnt
'''


def input_2d_array(Row, Column):
    array = generate_2d_array(Row, Column, 0)

    for i in range(Column):
        temp = list(map(int, input().split()))
        for j in range(Row):
            array[i][j] = temp[j]

    return array


def __starting_point():
    N, M = map(int, input().split())

    sc = input_2d_array(2, M)
    # print(sc)

    if M == 0 and N != 1:
        print(10**(N - 1))
        return

    '''if N == 1:
        flag = True
        for i in reversed(range(10)):
            for j in range(M):
                if i == sc[j][1] and flag:
                    flag = True
                else:
                    flag =False

            if flag == True and M != 0:
                print(sc[0][1])
                return
            else:
                print(-1)
                return

        print(0)
        return'''

    if N == 1:
        if M > 1:
            print(-1)
            return
        for i in range(10):
            for j in range(M):
                if i == sc[j][1]:
                    print(i)
                    return
        print(0)
        return

    ans = -1
    flag = True
    for i in reversed(range(10**(N - 1), 10**N)):
        for j in range(M):
            temp = str(i)
            # print('i=',i,'temp=',temp[sc[j][0]-1],'sc=',sc[j][1])
            if str(sc[j][1]) == temp[sc[j][0] - 1] and flag:
                flag = True
            else:
                flag = False

        if flag:
            ans = int(temp)

        flag = True

    print(ans)


__starting_point()

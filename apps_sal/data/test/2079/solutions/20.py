import sys
import math


def fun():
    n = int(input())
    arr = list(map(int, input().split()))
    enter_list = input()
    width_list = [[i + 1, arr[i]] for i in range(n)]
    width_list.sort(key=lambda x: x[-1])
    j = 0
    seated_list = [width_list[0]]
    all_list = [width_list[0][0]]
    j += 1
    for c in enter_list[1:]:
        if c == '0':
            seated_list.append(width_list[j])
            all_list.append(width_list[j][0])
            j += 1
        else:
            all_list.append(seated_list[-1][0])
            seated_list.pop()
    all_list = [str(i) for i in all_list]
    print(' '.join(all_list))


def __starting_point():
    fun()


__starting_point()

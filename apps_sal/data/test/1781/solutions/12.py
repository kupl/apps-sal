#   TaskB

import sys

n, k = list(map(int, sys.stdin.readline().split()))

my_list = list()

for i in range(n):
    my_list.append(input())


def left(i, my_list):
    return my_list[i] == '.' and \
        ((i - 1) < 0 or
            my_list[i - 1] == '.' or
            my_list[i - 1] == 'P' or
            my_list[i - 1] == '-' or
            my_list[i - 1] == 'x')


def right(i, my_list):
    return my_list[i] == '.' and \
        ((i + 1) >= len(my_list) or
            my_list[i + 1] == '.' or
            my_list[i + 1] == 'P' or
            my_list[i + 1] == '-' or
            my_list[i + 1] == 'x')


while k > 0:
    for index in range(n):
        cur_list = my_list[index]
        for i, _ in enumerate(cur_list):
            if left(i, cur_list) and right(i, cur_list):
                k = k - 1
                try:
                    part3 = cur_list[(i + 1):]
                except:
                    part3 = ''
                cur_list = cur_list[:i] + 'x' + part3
                my_list[index] = cur_list
                if k == 0:
                    break
            if k == 0:
                break
        if k == 0:
            break
    if k == 0:
        break

    for index in range(n):
        cur_list = my_list[index]
        for i, _ in enumerate(cur_list):
            if ((not left(i, cur_list) and cur_list[i] == '.') and right(i, cur_list)) or (left(i, cur_list) and (not right(i, cur_list)) and cur_list[i] == '.'):
                k = k - 1
                try:
                    part3 = cur_list[(i + 1):]
                except:
                    part3 = ''
                cur_list = cur_list[:i] + 'x' + part3
                my_list[index] = cur_list
                if k == 0:
                    break
            if k == 0:
                break
        if k == 0:
            break
    if k == 0:
        break

    for index in range(n):
        cur_list = my_list[index]
        for i, _ in enumerate(cur_list):
            if cur_list[i] == '.':
                k = k - 1
                try:
                    part3 = cur_list[(i + 1):]
                except:
                    part3 = ''
                cur_list = cur_list[:i] + 'x' + part3
                my_list[index] = cur_list
                if k == 0:
                    break
            if k == 0:
                break
        if k == 0:
            break
    if k == 0:
        break
    break

neighbours = 0
for i in range(n):
    cur_list = my_list[i]
    for j, _ in enumerate(cur_list):
        if cur_list[j] == 'S':
            if j - 1 >= 0 and (cur_list[j - 1] == 'x' or cur_list[j - 1] == 'P' or cur_list[j - 1] == 'S'):
                neighbours += 1
            if j + 1 <= len(cur_list) - 1 and (cur_list[j + 1] == 'x' or cur_list[j + 1] == 'P' or cur_list[j + 1] == 'S'):
                neighbours += 1
print(neighbours)
for i in range(n):
    print(my_list[i])

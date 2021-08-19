#!/usr/bin/env python3
def read_string():
    return input()


def read_strings(return_type=iter, split=None, skip=0):
    return return_type(input().split(split)[skip:])


def read_lines(height, return_type=iter):
    return return_type(read_string() for i in range(height))


def read_number():
    return int(input())


def read_numbers(return_type=iter, skip=0):
    return return_type(int(i) for i in input().split()[skip:])


def read_values(*types, array=None):
    line = input().split()
    result = []
    for return_type, i in zip(types, list(range(len(types)))):
        result.append(return_type(line[i]))
    if array != None:
        array_type, array_contained = array
        result.append(array_type(array_contained(i) for i in line[len(types):]))
    return result


def read_array(item_type=int, return_type=iter, skip=0):
    return return_type(item_type(i) for i in input().split()[skip:])


def read_martix(height, **args):
    return_type = args["return_type"] if "return_type" in args else iter
    return_type_inner = args["return_type_inner"] if "return_type_inner" in args else return_type
    return_type_outer = args["return_type_outer"] if "return_type_outer" in args else return_type
    item_type = args["item_type"] if "item_type" in args else int
    return return_type_outer(read_array(item_type=item_type, return_type=return_type_inner) for i in range(height))


def read_martix_linear(width, skip=0, item_type=int, skiped=None):
    num = read_array(item_type=item_type, skip=skip)
    height = len(num) / width
    return [num[i * width: (i + 1) * width] for i in range(height)]


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def main():
    n = read_number()
    arr = sorted(read_numbers(list))
    sum_x = sum(arr)
    sum_xy = 0
    for i in range(1, n):
        sum_xy += (arr[i] - arr[i - 1]) * i * (n - i)
    nu = sum_x + sum_xy * 2
    de = n
    g = gcd(nu, de)
    nu //= g
    de //= g
    print(nu, de)


def __starting_point():
    main()


__starting_point()

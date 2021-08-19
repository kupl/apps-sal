import collections
import math
import sys
production = True


def input(input_format=0, multi=0):
    if multi > 0:
        return [input(input_format) for i in range(multi)]
    else:
        next_line = sys.stdin.readline()[:-1]
        if input_format >= 10:
            use_list = False
            input_format = int(str(input_format)[-1])
        else:
            use_list = True
        if input_format == 0:
            formatted_input = [next_line]
        elif input_format == 1:
            formatted_input = list(map(int, next_line.split()))
        elif input_format == 2:
            formatted_input = list(map(float, next_line.split()))
        elif input_format == 3:
            formatted_input = list(next_line)
        elif input_format == 4:
            formatted_input = list(map(int, list(next_line)))
        elif input_format == 5:
            formatted_input = next_line.split()
        else:
            formatted_input = [next_line]
        return formatted_input if use_list else formatted_input[0]


def out(output_line, output_format=0, newline=True):
    formatted_output = ''
    if output_format == 0:
        formatted_output = str(output_line)
    elif output_format == 1:
        formatted_output = ' '.join(map(str, output_line))
    elif output_format == 2:
        formatted_output = '\n'.join(map(str, output_line))
    print(formatted_output, end='\n' if newline else '')


def log(*args):
    if not production:
        print('$$$', end='')
        print(*args)


enu = enumerate


def ter(a, b, c):
    return b if a else c


def ceil(a, b):
    return -(-a // b)


def mapl(iterable, format=0):
    if format == 0:
        return list(map(int, iterable))
    elif format == 1:
        return list(map(str, iterable))
    elif format == 2:
        return list(map(list, iterable))


def solve():
    n = input(11)
    a = input(1)
    t = 0
    for (i, j) in enu(a):
        if j != 1:
            out(ter(i & 1, 'Second', 'First'))
            return
    else:
        out(ter(n & 1, 'First', 'Second'))
    return


for i in range(input(11)):
    solve()

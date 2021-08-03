#
#    ------------------------------------------------
#           ____          _     Generatered using
#          / ___|        | |
#         | |    __ _  __| | ___ _ __  ______ _
#         | |   / _` |/ _` |/ _ \ '_ \|_  / _` |
#         | |__| (_| | (_| |  __/ | | |/ / (_| |
#          \____\____|\____|\___|_| |_/___\____|
#
#      GNU Affero General Public License v3.0
#    ------------------------------------------------
#    Author   : prophet
#    Created  : 2020-07-12 11:19:01.523119
#    UUID     : aXsU7xuXyjk3Ky2f
#    ------------------------------------------------
#
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

    formatted_output = ""

    if output_format == 0:
        formatted_output = str(output_line)
    elif output_format == 1:
        formatted_output = " ".join(map(str, output_line))
    elif output_format == 2:
        formatted_output = "\n".join(map(str, output_line))

    print(formatted_output, end="\n" if newline else "")


def log(*args):
    if not production:
        print("$$$", end="")
        print(*args)


enu = enumerate


def ter(a, b, c): return b if a else c


def ceil(a, b): return -(-a // b)


def mapl(iterable, format=0):

    if format == 0:
        return list(map(int, iterable))
    elif format == 1:
        return list(map(str, iterable))
    elif format == 2:
        return list(map(list, iterable))
#
#   >>>>>>>>>>>>>>> START OF SOLUTION <<<<<<<<<<<<<<
#


def solve():

    s = input(3)

    u = [0] * 3

    for i in s:
        if i == "R":
            u[0] += 1
        elif i == "P":
            u[1] += 1
        elif i == "S":
            u[2] += 1

    log(u)
    y = 0
    p = 0

    for i, j in enu(u):
        if j > y:
            y = j
            p = i

    if p == 0:
        a = "P"
    elif p == 1:
        a = "S"
    elif p == 2:
        a = "R"

    out(a * len(s))

    return


for i in range(input(11)):
    solve()
# solve()

#
#   >>>>>>>>>>>>>>>> END OF SOLUTION <<<<<<<<<<<<<<<
#

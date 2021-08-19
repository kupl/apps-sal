from sys import *
from bisect import *
from collections import *
from itertools import *
from fractions import *
from datetime import *

Input = []

stdin = open('input.txt', 'r')
stdout = open('output.txt', 'w')

# for i, val in enumerate(array, start_i_value)


def Out(x):
    stdout.write(str(x) + '\n')


def In():
    return stdin.readline().strip()


def inputGrab():
    for line in stdin:
        Input.extend(map(str, line.strip().split()))


'''--------------------------------------------------------------------------------'''


def main():
    n = int(In())
    y = 2013

    Lst = []
    Max = -1
    for _ in range(n):
        Lst.append(list(map(int, In().split())))
        Max = max(Max, Lst[_][2])

    Lst.sort()

    Ans = Max
    for i in range(len(Lst) - 1):
        Tmp = Lst[i][2]
        for j in range(i + 1, len(Lst)):
            x = date(2013, Lst[i][0], Lst[i][1])
            y = date(2013, Lst[j][0], Lst[j][1])

            #print(x, y)

            if(x > (y - timedelta(days=Lst[j][3]))):
                Tmp += Lst[j][2]

        Ans = max(Ans, Tmp)

    Out(Ans)


def __starting_point():
    main()


__starting_point()

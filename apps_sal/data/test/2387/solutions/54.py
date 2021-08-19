#from collections import defaultdict, deque
#import itertools
#import numpy as np
#import re
import bisect


def main():
    N = int(input())
    SS = []
    for _ in range(N):
        SS.append(input())
    S = []
    for s in SS:
        while '()' in s:
            s = s.replace('()', '')
        S.append(s)
    # print(S)
    S = [s for s in S if s != '']
    sum_op = 0
    sum_cl = 0
    S_both_op = []
    S_both_cl = []
    for s in S:
        if not ')' in s:
            sum_op += len(s)
        elif not '(' in s:
            sum_cl += len(s)
        else:
            pos = s.find('(')
            if pos <= len(s) - pos:
                S_both_op.append((pos, len(s) - pos))  # closeのほうが少ない、'))((('など -> (2,3)
            else:
                S_both_cl.append((pos, len(s) - pos))  # closeのほうが多い、')))(('など -> (3,2)

    # S_both_opは、耐えられる中でより伸ばす順にしたほうがいい？
    # S_both_op.sort(key=lambda x: (x[0], x[0]-x[1]))  #closeの数が小さい順にsortかつclose-openが小さい=伸ばす側にsort
    # S_both_cl.sort(key=lambda x: (x[0], x[0]-x[1]))  #これもcloseの数が小さい順にsortかつclose-openが小さい=あまり縮まない順にsort
    S_both_op.sort(key=lambda x: x[0])
    S_both_cl.sort(key=lambda x: -x[1])

    for p in S_both_op:
        sum_op -= p[0]
        if(sum_op < 0):
            print('No')
            return
        sum_op += p[1]

    for p in S_both_cl:
        sum_op -= p[0]
        if(sum_op < 0):
            print('No')
            return
        sum_op += p[1]

    if sum_op == sum_cl:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()

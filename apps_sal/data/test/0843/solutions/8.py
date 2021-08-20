from sys import stdin as Si
from math import floor as F
from collections import defaultdict as dt
from operator import itemgetter as ig


def __starting_point():
    n = int(Si.readline())
    d = Si.readline().strip('\n')
    c = tuple(map(int, Si.readline().split()))
    (tub, i, Exit) = (set([0]), 0, False)
    while not Exit:
        if d[i] == '>':
            i = i + c[i]
        else:
            i = i - c[i]
        if i < 0 or i >= n:
            print('FINITE')
            break
        elif i in tub:
            print('INFINITE')
            break
        else:
            tub.add(i)


'\nA. Little Artem and Grasshopper\ntime limit per test\n2 seconds\nmemory limit per test\n256 megabytes\ninput\nstandard input\noutput\nstandard output\n\nLittle Artem found a grasshopper. He brought it to his house and constructed a jumping area for him.\n\nThe area looks like a strip of cells 1\u2009×\u2009n. Each cell contains the direction for the next jump and the length of that jump. Grasshopper starts in the first cell and follows the instructions written on the cells. Grasshopper stops immediately if it jumps out of the strip. Now Artem wants to find out if this will ever happen.\nInput\n\nThe first line of the input contains a single integer n (1\u2009≤\u2009n\u2009≤\u2009100\u2009000) — length of the strip.\n\nNext line contains a string of length n which consists of characters "<" and ">" only, that provide the direction of the jump from the corresponding cell. Next line contains n integers di (1\u2009≤\u2009di\u2009≤\u2009109) — the length of the jump from the i-th cell.\nOutput\n\nPrint "INFINITE" (without quotes) if grasshopper will continue his jumps forever. Otherwise print "FINITE" (without quotes).\nExamples\nInput\n\n2\n><\n1 2\n\nOutput\n\nFINITE\n\nInput\n\n3\n>><\n2 1 1\n\nOutput\n\nINFINITE\n\nNote\n\nIn the first sample grasshopper starts from the first cell and jumps to the right on the next cell. When he is in the second cell he needs to jump two cells left so he will jump out of the strip.\n\nSecond sample grasshopper path is 1 - 3 - 2 - 3 - 2 - 3 and so on. The path is infinite.\n'
__starting_point()

import sys
import math
import heapq
import random
import collections
import bisect


def main():

    st = input()
    count = 0

    while st.find('bear') != -1:
        idx = st.find('bear')
        count = ((idx + 1) * (len(st) - (3 + idx))) + count
        st = st[idx + 1:]

    print(count)


def __starting_point():
    main()


__starting_point()

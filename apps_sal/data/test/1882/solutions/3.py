# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 18:46:09 2018

@author: Sand Boa
"""

import sys
import operator  # itemgetter
import itertools  # islice


def __starting_point():
    n, T = list(map(int, input().split()))
    listi = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        listi.append((a, b, i))
    # print(listi)
    listi = sorted(listi, key=lambda x: x[1])
    # print(listi)
    time = [0] * (n + 1)
    count = [0] * (n + 1)
    time_sum = 0
    count_sum = 0
    k = 1

    for (a, t, ind) in listi:
        if k <= a:
            time[a] += t
            time_sum += t
            if time_sum > T:
                break

            count[a] += 1
            count_sum += 1
            if count_sum == k:
                count_sum -= count[k]
                time_sum -= time[k]
                k += 1

    max_score = max(count_sum, k - 1)
    #max_score = count_sum

    print(max_score)
    print(max_score)
    print((*list(itertools.islice(
        (idx + 1 for (a, t, idx) in listi if a >= max_score),
        max_score
    ))))
    # print(listi)
    '''for a, t, idx in listi:
        if idx > max_score:
            print(idx,sep=" ")
            '''
    # print(idx+1 for  in listi )


__starting_point()

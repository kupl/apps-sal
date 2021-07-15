#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codeforces Round #552 (Div. 3)

Problem E. Two Teams

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""

__version__ = '1.0'
__date__ = '2019-04-17'

import sys


def remove_me(to_left, to_right, index):
    left_id = to_left[index]
    right_id = to_right[index]
    if right_id < len(to_left):
        to_left[right_id] = left_id
    if left_id >= 0:
        to_right[left_id] = right_id
    return (left_id, right_id)

def join_team(n, k, students):
    teams = ['0'] * n
    mydict = dict(list(zip(students, list(range(n)))))    # {skill: id}
    to_left = [i-1 for i in range(n)]
    to_right = [i+1 for i in range(n)]

    next_chosen = n
    chosen_total = 0
    while chosen_total < n:
        for couch in ['1', '2']:
            while teams[mydict[next_chosen]] != '0':
                next_chosen -= 1
                if next_chosen < 1:
                    return teams
            teams[mydict[next_chosen]] = couch
            chosen_total += 1
            left_id, right_id = remove_me(to_left, to_right,
                                          mydict[next_chosen])
            for i in range(k):
                if left_id < 0:
                    break
                teams[left_id] = couch
                chosen_total += 1
                left_id, right_id = remove_me(to_left, to_right, left_id)
            for i in range(k):
                if right_id >= n:
                    break
                teams[right_id] = couch
                chosen_total += 1
                left_id, right_id = remove_me(to_left, to_right, right_id)
    return teams

def main(argv=None):
    n, k = list(map(int, input().split()))
    students = list(map(int, input().split()))
    print(''.join(join_team(n, k, students)))
    return 0

def __starting_point():
    STATUS = main()
    return(STATUS)


__starting_point()

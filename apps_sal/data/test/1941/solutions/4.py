# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 01:59:52 2015

codeforces 299 Div 2 C
"""
import sys


def read_data():
    A, B, n = list(map(int, input().split()))
    ltm = sys.stdin.readlines()
    return A, B, ltm


def solve(A, B, ltm):
    for line in ltm:
        L, t, m = list(map(int, line.split()))
        print(max_r(L, t, m, A, B))


memo = dict()


def max_r(L, t, m, A, B):
    nonlocal memo
    if (L, t, m) in memo:
        return memo[L, t, m]
    r_upper = (t - A) // B + 2
    if r_upper <= L:
        memo[L, t, m] = -1
        return -1
    r_lower = L
    threshold = t * m
    while r_upper > r_lower + 1:
        mid = (r_upper + r_lower) // 2
        if (2 * A + B * (L + mid - 2)) * (mid - L + 1) // 2 <= threshold:
            r_lower = mid
        else:
            r_upper = mid
    memo[L, t, m] = r_lower
    return r_lower


A, B, ltm = read_data()
solve(A, B, ltm)

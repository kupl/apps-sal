#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codeforces Round #553 (Div. 2)

Problem F. Sonya and Informatics

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""

__version__ = '1.8'
__date__ = '2019-04-21'

import sys


def binom_dp():
    dp = [[-1 for j in range(110)] for i in range(110)]
    def calculate(n, k):
        if n < k:
            return 0
        if n == k or k == 0:
            return 1
        if dp[n][k] > 0:
            return dp[n][k]
        else:
            dp[n][k] = calculate(n-1, k-1) + calculate(n-1, k)
        return dp[n][k]
    return calculate

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def multiply(A, B, mod):
    if not hasattr(B[0], '__len__'):
        C = [sum(aij * B[j] % mod for j, aij in enumerate(ai)) for ai in A]
    else:
        C = [[0 for col in range(len(B[0]))] for row in range(len(A))]
        len_A = len(A)
        len_B = len(B)
        for row in range(len_A):
            if sum(A[row]) == 0:
                continue
            for col in range(len_B):
                C[row][col] = sum(A[row][k] * B[k][col]
                                  for k in range(len_B)) % mod
    return C

def memoize(func):
    memo = {}
    def wrapper(*args):
        M, n, mod = args
        if n not in memo:
            memo[n] = func(M, n, mod)
        return memo[n]
    return wrapper

@memoize
def matrix_pow(M, n, mod):
    # print(f'n is {n}')
    if n == 2:
        return multiply(M, M, mod)
    if n == 1:
        return M
    sub_M = matrix_pow(M, n//2, mod)
    if n % 2 == 0:
        return multiply(sub_M, sub_M, mod)
    return multiply(sub_M, matrix_pow(M, n - n//2, mod), mod)

def solve(n, k, a, binom, mod):
    ones = sum(a)
    zeros = n - ones
    M = [[0 for col in range(zeros+1)] for row in range(zeros+1)]
    for row in range(max(0, zeros-ones), zeros+1):
        pre_zeros = row
        pre_ones = zeros - pre_zeros
        post_zeros = pre_ones
        post_ones = ones - pre_ones
        M[row][row] = (pre_ones * post_ones + pre_zeros * post_zeros
                       + binom(zeros, 2) + binom(ones, 2))
        if row > max(0, zeros-ones):
            M[row-1][row] = pre_zeros * post_ones
        if row < zeros:
            M[row+1][row] = post_zeros * pre_ones
    M = [matrix_pow(M, k, mod)[-1]]
    b = [0] * (zeros + 1)
    b[zeros - sum(a[:zeros])] = 1
    C = multiply(M, b, mod)
    return C[-1]


def main(argv=None):
    mod = int(1e9) + 7
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    binom = binom_dp()
    P = solve(n, k, a, binom, mod)
    if P == 0:
        print(0)
    else:
        Q = pow(binom(n, 2), k, mod)
        print(P * modinv(Q, mod) % mod)
    return 0


def __starting_point():
    STATUS = main()
    return(STATUS)


__starting_point()

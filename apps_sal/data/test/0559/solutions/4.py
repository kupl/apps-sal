# -*- coding: utf-8 -*-
from sys import stdin
import numpy as np
# import sys
# sys.setrecursionlimit(10**4)
# import time

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list([int(x)-1 for x in stdin.readline().split()])
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]


p = _i()
a_list = np.array(_li())

factorial_invs = {0: 1, 1: 1}
for i in range(2, p):
    factorial_invs[i] = (factorial_invs[i-1] * pow(i, p-2, p)) % p
np_fact_invs = np.tile(np.array(list(factorial_invs.values()))
                       .reshape(1, -1), (p, 1))

pow_table = np.ones((p, p), dtype=int)
pow_table[1, :] = np.arange(p)
for i in range(2, p):
    pow_table[i] = (pow_table[i-1] * pow_table[1]) % p
pow_table = pow_table.T

fact_pminus1 = pow(factorial_invs[p-1], p-2, p)

coefs = np.zeros(p, dtype=int)
# for i, a in enumerate(a_list):
#     if a == 1:
#         for k in range(1, p):
#             coefs[k] = coefs[k] - (-1)**(k % 2) * pow(i, p-1-k, p)\
#                     * fact_pminus1\
#                     * factorial_invs[k]\
#                     * factorial_invs[p-1-k]
#             coefs[k] %= p

coefs[0] = a_list[0]
sign_array = np.tile(((-1) ** (np.arange(1, p) % 2)).reshape(1, -1), (p, 1))
coefs[1:] = - ((((sign_array[a_list == 1, :]
                  * pow_table[a_list == 1, :-1][:, ::-1]
                  * fact_pminus1) % p
                 * np_fact_invs[a_list == 1, 1:]) % p
                * np_fact_invs[a_list == 1, :-1][:, ::-1]
                ) % p).sum(axis=0)
coefs %= p

print((*coefs))


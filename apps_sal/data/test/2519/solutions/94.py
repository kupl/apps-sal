import os
import sys
import re
import math


def get_exp_value(number):
    if number == 0:
        return 0
    a = (number + 1) / number
    exp = a * (number // 2)
    if number % 2 != 0:
        exp += a / 2

    return exp


(N, K) = [int(n) for n in input().split()]
P = [int(n) for n in input().split()]

exps = [get_exp_value(i) for i in range(200001)]

s = sum(P[0:K])
max_sum = 0
max_pos = 0
for i in range(K, N):
    s = s - P[i - K] + P[i]
    if s > max_sum:
        max_sum = s
        max_pos = i

answer = 0
for i in range(max_pos - K, max_pos):
    answer += exps[P[i + 1]]

print(answer)

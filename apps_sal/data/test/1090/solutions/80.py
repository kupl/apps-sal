import sys
import math
import collections
import itertools
input = sys.stdin.readline
(N, K) = list(map(int, input().split()))
S = input().rstrip()
ori_num = 0
turn_num = 0
for i in range(N):
    if i > 0:
        if S[i - 1] == 'L' and S[i] == 'L':
            ori_num += 1
        if S[i - 1] != S[i]:
            turn_num += 1
    if i < N - 1:
        if S[i] == 'R' and S[i + 1] == 'R':
            ori_num += 1
if turn_num >= 2 * K:
    ori_num += 2 * K
else:
    num = turn_num // 2
    num2 = turn_num % 2
    ori_num += 2 * num + num2
print(ori_num)

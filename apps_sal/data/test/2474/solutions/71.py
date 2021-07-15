# coding: utf-8

import itertools
import sys

N = int(input())
C = [int(x) for x in input().split()]

# Cを昇順にソートしておく
C.sort()

# （C_iの個数×C_iのコスト）の総和×2**Nを求める
sum = 0
for i in range(N):
	sum += (N + 1 - i) * C[i]
sum *= 2 ** (N - 2)
sum *= 2 ** N

# 10**9 + 7で割った余りを求めて出力
print(int(sum % (10 ** 9 + 7)))

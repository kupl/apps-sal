# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:37:37 2020

@author: liang
"""

"""
フィボナッチ数列生成
【DP(?)】　: 配列を使用することで計算量が爆発するのを防ぐ
【小さいものから計算する】の原則

【方針】
　通常の配列を用いたフィボナッチ数列の生成方法の応用版
 壊れた階段のフィボナッチ数列の値を　0 にすることで、実質遷移を止めることが出来る。
"""
key = 10**9 + 7
N, M = map(int, input().split())
A = [int(input()) for _ in range(M)] + [-1]

fibs = [0] * (N + 1)
index = 0
for i in range(N + 1):
    # 壊れたところの値を0にすれば良い
    if i == A[index]:
        fibs[i] = 0
        index += 1
    elif i == 0 or i == 1:
        fibs[i] = 1
    else:
        fibs[i] = (fibs[i - 1] + fibs[i - 2]) % key


print(fibs[N])

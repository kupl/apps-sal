#!/usr/bin python3
# -*- coding: utf-8 -*-

n, k = list(map(int, input().split()))
s = input()

if n==1:
    print(s)
    return



dic={}
dic['RR'] = 'R'
dic['SS'] = 'S'
dic['PP'] = 'P'
dic['RP'] = 'P'
dic['PR'] = 'P'
dic['PS'] = 'S'
dic['SP'] = 'S'
dic['RS'] = 'R'
dic['SR'] = 'R'

dp = [[-1]*n for i in range(110)]
# dp[i][j]  i番目の高さで左端がjとなる場合の勝者

ss = s*2
for i in range(n):
    dp[1][i]=dic[ss[i:i+2]]

def f(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = dic[f(i-1, j)+f(i-1, (pow(2,i-1)+j)%n)]
        return dp[i][j]


print((f(k,0)))


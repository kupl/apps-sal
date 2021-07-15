#!/usr/bin python3
# -*- coding: utf-8 -*-
# 桁DP
# 1以上n以下の整数であって、 10進法で表したときに、0でない数字がちょうど
# k個あるようなものの個数

n = input()
k = int(input())
l = len(n)
#dp[i][j][status]   status=0 は小さいのが未確定=i文字まで同じ
#                   status=1 は小さいことが確定
# i桁目まで決めて、0でない桁がj個
# 初期値は1 からスタート s=0,i=0,j=0
dp = [[[0]*2 for j in range(k+1)] for i in range(l+1)]
dp[0][0][0] = 1
for i in range(l):
    ni = int(n[i])
    for j in range(k+1):
        for st in range(2):
            for x in range(10):
                i_ = i+1
                j_ = j
                st_ = st
                if x != 0:
                    j_ += 1
                if j_ > k:
                    continue
                if st_ == 0 and x > ni:
                    continue
                if st_ == 0 and x < ni:
                    st_ = 1
                dp[i_][j_][st_] += dp[i][j][st]

print((sum(dp[l][k])))


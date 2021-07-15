# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:38:11 2020

@author: liang
"""

"""
＜D - Multiple of 2019>
【方針】
a = b(mod2019) => a - b は　2019の倍数
余りが等しいグループの組み合わせの総数が解になる。
既に2019の倍数であるものは単体で成立するため、[0]のカウントを一つあげておく


＜累積和＞
【計算量削減】
大きな数を使わない　⇒　mod を使う
tmp += 7 * 100000000  => 7 * ( 2019*N + α) => 7 * α　と同じ
　　⇒　累乗(10**N) に  mod をかけると良い

100000000 + γ => (2019*N + β) + γ => β + γ と同じ
　⇒　累積和　に　mod をかけると良い
 
 for文で１文字ずつ足し算していくことで実装可能
 
 reversed() : 逆順に並べ替え
 reversed(input()) : 入力を逆順に取り出す
 
"""
S = input()

MOD = 2019 

counter = [0] * 2019
counter[0] = 1
t = 1
tmp = 0
for i in reversed(S):
    tmp += int(i)*t
    tmp %= MOD #累積和を効率化
    t *= 10
    t %= MOD   #累乗を効率化 
    #print(tmp)
    counter[tmp] += 1

ans = sum( i*(i-1)//2 for i in counter)
print(ans)

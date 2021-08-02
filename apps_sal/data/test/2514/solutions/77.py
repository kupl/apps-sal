# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 01:13:08 2020

@author: liang
"""
"""
ABC  171 D 差分更新　パケット変換
【無駄な探索は行わない（メモリ化） ⇒　パケット変換】
パケット
　値vが出現する回数を記録しておく

dict()方式　⇒　探索にO(logn) or O(n)がかかる
配列方式　⇒　探索がO(1)となる!

【差分更新】
値Bが全て値Cになる
　⇒　(C - B) * 値Bの個数だけ増加する
 ⇒　値Cの個数　+= 値Bの個数
 ⇒　値Bの個数　= 0
"""

N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())

d = [0] * (10**5)

for i in A:
    d[i - 1] += 1

ans = sum(A)

for i in range(Q):
    b, c = map(int, input().split())
    ans += (c - b) * d[b - 1]
    d[c - 1] += d[b - 1]
    d[b - 1] = 0
    print(ans)

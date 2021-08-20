"""
Created on Mon Sep  7 01:13:08 2020

@author: liang
"""
'\nABC  171 D 差分更新\u3000パケット変換\n【無駄な探索は行わない（メモリ化） ⇒\u3000パケット変換】\nパケット\n\u3000値vが出現する回数を記録しておく\n\ndict()方式\u3000⇒\u3000探索にO(logn) or O(n)がかかる\n配列方式\u3000⇒\u3000探索がO(1)となる!\n\n【差分更新】\n値Bが全て値Cになる\n\u3000⇒\u3000(C - B) * 値Bの個数だけ増加する\n ⇒\u3000値Cの個数\u3000+= 値Bの個数\n ⇒\u3000値Bの個数\u3000= 0\n'
N = int(input())
A = [int(i) for i in input().split()]
Q = int(input())
d = [0] * 10 ** 5
for i in A:
    d[i - 1] += 1
ans = sum(A)
for i in range(Q):
    (b, c) = map(int, input().split())
    ans += (c - b) * d[b - 1]
    d[c - 1] += d[b - 1]
    d[b - 1] = 0
    print(ans)

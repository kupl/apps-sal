# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 01:01:58 2020

@author: liang
"""
#ゼロパディング＋インデックス
#str(1).zfill(6) + str(a.index(2) + 1).zfill(6)
#index(x) が重い => indexを使わなくて良いようにする

N, M = map(int, input().split())
#d = [list() for _ in range(N)]
dic = dict()
dic2 = dict()
P = list()

#insert O(M)
for i in range(M):
    p, y = map(int,input().split())
    #d[p-1].append(y)
    if p not in dic.keys():
        dic[p] = [y]
    else:
        dic[p].append(y)
    P.append((p,y))

#year sort O(N log N) => 重い　dict使用
#for i in range(N):
#    d[i].sort()
for key in dic.keys():
    dic[key].sort()

for key in dic.keys():
    for i in range(len(dic[key])):
        dic2[dic[key][i]] = i+1
#search O(M)***
for i in range(M):
    p, y = P[i]
    ans = str(p).zfill(6)+str(dic2[y]).zfill(6)
    """
    # zfill 重い？
    ans = ''
    ans += '0'*( 6 - len(str(p))) + str(p)
    #t = dic[p].index(y)+1
    t = dic2[y]
    ans += '0'*( 6 - len(str(t))) + str(t)
    """
    print(ans)

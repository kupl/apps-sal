"""
Created on Tue Sep 15 01:01:58 2020

@author: liang
"""
(N, M) = map(int, input().split())
dic = dict()
dic2 = dict()
P = list()
for i in range(M):
    (p, y) = map(int, input().split())
    if p not in dic.keys():
        dic[p] = [y]
    else:
        dic[p].append(y)
    P.append((p, y))
for key in dic.keys():
    dic[key].sort()
for key in dic.keys():
    for i in range(len(dic[key])):
        dic2[dic[key][i]] = i + 1
for i in range(M):
    (p, y) = P[i]
    ans = ''
    ans += '0' * (6 - len(str(p))) + str(p)
    t = dic2[y]
    ans += '0' * (6 - len(str(t))) + str(t)
    print(ans)

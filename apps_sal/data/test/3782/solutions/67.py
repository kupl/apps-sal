# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7
input = lambda: sys.stdin.readline().rstrip()
YesNo = lambda b: bool([print('Yes')] if b else print('No'))
YESNO = lambda b: bool([print('YES')] if b else print('NO'))
int1 = lambda x: int(x) - 1

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
if Q == 1:
    print(0)
    return()
ans = INF
for i, Y in enumerate(A):
    seqs = []
    tmp = []
    for j, x in enumerate(A):
        if i == j:
            continue
        if x >= Y:
            tmp.append(x)
        else:
            if tmp:
                tmp.sort()
                seqs.append(tmp)
                tmp = []
    if tmp:
        tmp.sort()
        seqs.append(tmp)
    l = []
    for seq in seqs:
        if len(seq) >= K:
            l.extend(seq[:(len(seq) - K + 1)])
    l.sort()
    if len(l) >= Q - 1:
        X = l[Q - 2]
        ans = min(ans, X - Y)
print(ans)

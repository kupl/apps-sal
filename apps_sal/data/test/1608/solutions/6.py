# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)


def getMul(x):
    a = 1
    for xi in x:
        a *= xi
    return a


n = int(input())
a = list(map(int, input().split()))
d = {}
for ai in a:
    if ai in d: d[ai] += 1
    else: d[ai] = 1

f = [[] for i in range(max(a) + 10)]
for i in range(1, len(f)):
    for j in range(i, len(f), i):
        f[j].append(i)

seq = [0 for i in range(max(a) + 10)]
for ai in d:
    for fi in f[ai]:
        seq[fi] += d[ai]
for i in range(len(seq)):
    seq[i] = (pow(2, seq[i], MOD) - 1 + MOD) % MOD

pf = [[] for i in range(max(a) + 10)]
pf[0] = None
pf[1].append(1)
for i in range(2, len(f)):
    if len(pf[i]) == 0:
        for j in range(i, len(pf), i):
            pf[j].append(i)
for i in range(1, len(pf)):
    mul = getMul(pf[i])
    if mul == i:
        if len(pf[i]) & 1 == 1: pf[i] = -1
        else: pf[i] = 1
    else:
        pf[i] = 0
pf[1] = 1

ans = 0
for i in range(1, len(seq)):
    ans += seq[i] * pf[i]
    ans = (ans + MOD) % MOD
print(ans)

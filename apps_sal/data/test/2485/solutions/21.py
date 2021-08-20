import collections
import sys
import math
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return map(int, input().split())


def LIST():
    return list(MAP())


def NIJIGEN(H):
    return [list(input()) for i in range(H)]


(H, W, M) = map(int, input().split())
A = list()
B = list()
for i in range(M):
    (a, b) = map(int, input().split())
    A.append(a)
    B.append(b)
c = collections.Counter(A)
s = c.most_common()
k = s[0][0]
t = s[0][1]
L = list()
for i in range(M):
    if A[i] != k:
        L.append(B[i])
c = collections.Counter(L)
s = c.most_common()
if len(s) != 0:
    ans = s[0][1] + t
else:
    ans = t
c = collections.Counter(B)
s = c.most_common()
k = s[0][0]
t = s[0][1]
L = list()
for i in range(M):
    if B[i] != k:
        L.append(A[i])
c = collections.Counter(L)
s = c.most_common()
if len(s) != 0:
    q = s[0][1] + t
else:
    q = t
ans = max(ans, q)
print(ans)

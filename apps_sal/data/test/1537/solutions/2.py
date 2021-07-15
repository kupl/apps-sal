from sys import stdin, stdout
from collections import *
from array import *
def iarr(delim = " "): return map(int, input().split(delim))
def mat(n, m, v = None): return [[v]*m for _ in range(n)]

n, k, *_ = iarr()
lc = [-1]*n
rc = [n]*n
tr = [-1]*n
br = [n]*n
b = [input() for _ in range(n)]
ans = mat(n, n, 0)
pre, post = 0, 0

for i, r in enumerate(b):
    for j, c in enumerate(r):
        if c == 'B':
            rc[i], br[j] = j, i
            if lc[i] == -1: lc[i] = j
            if tr[j] == -1: tr[j] = i
            
for i in range(n):
    if tr[i] == -1 and br[i] == n: pre += 1
    if lc[i] == -1 and rc[i] == n: pre += 1

for col in range(n-k+1):
    tot = 0
    for row in range(k):
        if lc[row] >= col and rc[row] < col+k: tot += 1
    ans[0][col] = tot
    for row in range(1, n-k+1):
        if lc[row-1] >= col and rc[row-1] < col+k: tot -= 1
        if lc[row+k-1] >= col and rc[row+k-1] < col+k: tot += 1
        ans[row][col] = tot

for row in range(n-k+1):
    tot = 0
    for col in range(k):
        tot += 1 if tr[col] >= row and br[col] < row+k else 0
    post = max(post, ans[row][0]+tot)
    for col in range(1, n-k+1):
        if tr[col-1] >= row and br[col-1] < row+k: tot -= 1
        if tr[col+k-1] >= row and br[col+k-1] < row+k: tot += 1
        post = max(post, ans[row][col]+tot)

print(pre+post)

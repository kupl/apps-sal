import sys
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**9)
h, w, d = list(map(int, input().split()))
inds = {}
for i in range(h):
    for D, j in enumerate(input().split()):
        inds[int(j) - 1] = (i, D)
nows = [[0]for c in range(d)]

for k in range(d, h * w):
    a, b = inds[k]
    x, y = inds[k - d]
    k %= d
    nows[k].append(nows[k][-1] + abs(a - x) + abs(b - y))
q = input()
for i in inputs():
    l, r = list(map(int, i.split()))
    l -= 1; r -= 1
    l, b = divmod(l, d)
    r, b = divmod(r, d)
    print((nows[b][r] - nows[b][l]))

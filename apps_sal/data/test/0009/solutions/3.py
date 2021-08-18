import bisect
import sys
try:
    fin = open('in')
except:
    fin = sys.stdin
input = fin.readline

d = int(input())
n, m = map(int, input().split())
x1, y1, x2, y2 = [], [], [], []
T = []
for _ in range(d):
    u, v, w, x = map(int, input().split())
    if u > w:
        u, w = w, u
    if v > x:
        v, x = x, v
    x1.append(u)
    y1.append(v)
    x2.append(-w)
    y2.append(-x)
    T.append([u, v, w, x])

x1.sort()
x2.sort()
y1.sort()
y2.sort()

req = list(map(int, input().split()))
for i in range(len(T)):
    u, v, w, x = T[i]
    if req[0] == bisect.bisect_left(x1, w) - (u != w):
        if req[1] == bisect.bisect_left(x2, -u) - (u != w):
            if req[2] == bisect.bisect_left(y1, x) - (v != x):
                if req[3] == bisect.bisect_left(y2, -v) - (v != x):
                    print(i + 1)
                    break
else:
    print(-1)

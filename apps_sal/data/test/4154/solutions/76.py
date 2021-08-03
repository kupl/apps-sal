import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L, R = [], []
for _ in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
l, r = max(L), min(R)
if l > r:
    print(0)
else:
    print(r - l + 1)

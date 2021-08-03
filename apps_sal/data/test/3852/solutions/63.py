import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
mx = -float("inf")
mn = float("inf")
mxi = 0
mni = 0
for i in range(N):
    x = a[i]
    if mx < x:
        mx = x
        mxi = i
    if mn > x:
        mn = x
        mni = i
print(2 * N - 1)
if abs(mx) > abs(mn):
    for i in range(N):
        print(mxi + 1, i + 1)
    for i in range(N - 1):
        print(i + 1, i + 2)
else:
    for i in range(N):
        print(mni + 1, i + 1)
    for i in range(N - 1, 0, -1):
        print(i + 1, i)

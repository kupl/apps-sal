import sys

N = int(input())
a = [0]
a[1:] = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
mys = 0
for i in range(1, N + 1):
    mys = max(mys, a[i])
    if mys <= i:
        ans += 1
print(ans)

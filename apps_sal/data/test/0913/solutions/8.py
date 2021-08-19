import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
(pa, pb) = (0, 0)
for i in range(n):
    if a[i] == 0 and b[i] == 1:
        pb += 1
    if a[i] == 1 and b[i] == 0:
        pa += 1
if pa == 0:
    print(-1)
else:
    ans = 1 * pb // pa + 1
    print(ans)

import sys

n, m = map(int, sys.stdin.readline().split())

l = 1
r = n
for i in range(m):
    new_l, new_r =  map(int, sys.stdin.readline().split())
    if new_l > l:
        l = new_l
    if new_r < r:
        r = new_r
ans = max(0, r - l + 1)
print(ans)

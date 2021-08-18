from sys import stdin
import sys
n = int(stdin.readline().strip())
s = tuple(map(int, stdin.readline().strip().split()))
if s[0] != 0:
    print(1)
    return
x = 1
ans = -1
for i in range(1, n):
    if s[i] <= x:
        x = max(x, s[i] + 1)
    else:
        ans = i + 1
        break
print(ans)

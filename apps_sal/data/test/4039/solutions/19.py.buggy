from math import gcd, sqrt
import sys
input = sys.stdin.readline


n, r = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
p = 0
while (p < n):
    if l[p][0] <= r and l[p][1] >= 0:
        r += l[p][1]
        l = l[:p] + l[p + 1:]
        p = 0
        n -= 1
    else:
        p += 1
if l == []:
    print("YES")
    return
ans = True
q = len(l)
for i in range(q):
    l[i][0] = max(l[i][0], -l[i][1])
l = sorted(l, key=lambda x: x[0] + x[1])
l.reverse()
#print(l, r)
for i in range(len(l)):
    if l[i][0] > r:
        ans = False
        break
    else:
        r += l[i][1]
if ans and r >= 0:
    print("YES")
else:
    print("NO")
